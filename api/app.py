
from flask import Flask, request, jsonify
from sqlalchemy import exc
from flask_sqlalchemy import SQLAlchemy

from model.model import Base
from model.room import Room
from model.user import User
from model.prediction import Prediction, Question


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


@app.before_first_request
def setup():
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)


@app.route('/room/add', methods=['POST'])
def add_room():
    try:
        new_room = Room(name=request.form['name'])
        db.session.add(new_room)
        db.session.commit()
        return jsonify(new_room.json), 201

    except exc.IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Room "{}" already exists'.format(request.form['name'])}), 403


@app.route('/room/<int:room_id>/user/add', methods=['POST'])
def add_user(room_id):
    room = db.session.query(Room).get(room_id)
    if room:
        try:
            predictions_json = request.form['predictions']
            try:
                Prediction(predictions_json)
            except (ValueError, TypeError):
                return jsonify({'error': 'Invalid predictions format'}), 400

            new_user = User(name=request.form['name'], room_id=room_id, predictions_json=predictions_json)
            db.session.add(new_user)
            db.session.commit()
            return jsonify(new_user.json), 201

        except exc.IntegrityError:
            db.session.rollback()
            return jsonify({'error': 'User "{}" already exists'.format(request.form['name'])}), 403

    else:
        return jsonify({'error': 'room not found'}), 404


@app.route('/room/<int:room_id>/users')
def get_users(room_id):
    room = db.session.query(Room).get(room_id)
    if room:
        return jsonify([user.json for user in room.users])

    else:
        return jsonify({'error': 'Room not found'}), 404


@app.route('/questions')
def get_all_questions():
    return jsonify(Question.get_all_questions())


if __name__ == "__main__":
    app.run()
