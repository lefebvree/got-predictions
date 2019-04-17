
from flask import Flask, request, jsonify
from sqlalchemy import exc
from flask_sqlalchemy import SQLAlchemy

from model.model import Base
from model.room import Room
from model.user import User
from model.prediction import Prediction, Character


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


@app.before_first_request
def setup():
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)

    p = Prediction(fates={Character.ARYA_STARK: {'death': True}})


@app.route('/room/add', methods=['POST'])
def add_room():
    try:
        new_room = Room(name=request.form['name'])
        db.session.add(new_room)
        db.session.commit()
        return jsonify(new_room.json), 201

    except exc.IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'room already exists'}), 403


@app.route('/room/<int:room_id>/user/add', methods=['POST'])
def add_user(room_id):
    room = db.session.query(Room).get(room_id)
    if room:
        try:
            new_user = User(name=request.form['name'], room_id=room_id)
            db.session.add(new_user)
            db.session.commit()
            return jsonify(new_user.json), 201

        except exc.IntegrityError:
            db.session.rollback()
            return jsonify({'error': 'user already exists'}), 403

    else:
        return jsonify({'error': 'room not found'}), 404


@app.route('/room/<int:room_id>/users')
def get_users(room_id):
    room = db.session.query(Room).get(room_id)
    if room:
        return jsonify([user.json for user in room.users])

    else:
        return jsonify({'error': 'room not found'}), 404


if __name__ == "__main__":
    app.run()
