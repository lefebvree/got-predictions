
from json import dumps

from flask import Flask, request, jsonify
from sqlalchemy import exc
from flask_sqlalchemy import SQLAlchemy

from model.model import Base
from model.room import Room
from model.user import User
from model.prediction import Prediction, Question
from settings import DB_FILE


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_FILE
db = SQLAlchemy(app)


# @app.before_first_request
# def setup():
#     Base.metadata.drop_all(bind=db.engine)
#     Base.metadata.create_all(bind=db.engine)


@app.route('/room/<string:room_name>', methods=['POST'])
def get_room(room_name):
    room_name = Room.clean_name(room_name)
    room = db.session.query(Room).get(room_name)
    if room:
        if room.password == request.form['password']:
            return jsonify(room.json)
        else:
            return jsonify({'error': 'Wrong password'}), 401
    else:
        return jsonify({'error': 'Room not found'}), 404


@app.route('/room/add', methods=['POST'])
def add_room():
    room_name = Room.clean_name(request.form['name'])
    if 4 > len(room_name) > 50:
        return jsonify({'error': 'Invalid room name'}), 403

    try:
        new_room = Room(name=room_name, password=request.form['password'])
        db.session.add(new_room)
        db.session.commit()
        return jsonify(new_room.json), 201

    except exc.IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Room "{}" already exists'.format(room_name)}), 403


@app.route('/room/<string:room_name>/user/add', methods=['POST'])
def add_user(room_name):
    room_name = Room.clean_name(room_name)
    user_name = request.form['name']
    room_password = request.form['password']
    predictions_json = request.form['predictions']

    room = db.session.query(Room).get(room_name)
    if room:
        if room.password == room_password:
            if 3 > len(user_name) > 25:
                return jsonify({'error': 'Invalid user name'.format(user_name)}), 403

            if user_name in map(lambda u: u.name, room.users):
                return jsonify({'error': 'User "{}" already exists'.format(user_name)}), 403

            if len(predictions_json) > 5000:
                return jsonify({'error': 'Invalid predictions format, too long'}), 400

            try:
                predictions = Prediction(predictions_json)
                predictions.remove_answered_questions()
            except (ValueError, TypeError) as e:
                print(e)
                return jsonify({'error': 'Invalid predictions format'}), 400

            filtered_json = dumps(predictions.json)

            new_user = User(name=user_name, room_id=room_name, predictions_json=filtered_json)
            db.session.add(new_user)
            db.session.commit()
            return jsonify(new_user.json), 201
        else:
            return jsonify({'error': 'Wrong password'}), 401
    else:
        return jsonify({'error': 'Room not found'}), 404


@app.route('/room/<string:room_name>/users')
def get_users(room_name):
    room_name = Room.clean_name(room_name)
    room = db.session.query(Room).get(room_name)
    if room:
        return jsonify([user.json for user in room.users])

    else:
        return jsonify({'error': 'Room not found'}), 404


@app.route('/questions')
def get_all_questions():
    return jsonify(Question.get_all_questions())


if __name__ == "__main__":
    app.run()
