
from sqlalchemy import Column, Integer, String, orm

from model.model import Base


class Room(Base):
    __tablename__ = 'room'

    name = Column(String(25), primary_key=True, nullable=False, unique=True)
    password = Column(String(25), nullable=False)
    users = orm.relationship('User', backref='room', lazy=True)

    @property
    def json(self):
        return {'name': self.name, 'users': {user.id: user.json for user in self.users}}

    @staticmethod
    def clean_name(room_name):
        ''.join(e for e in room_name if e.isalnum())
        return room_name.strip().lower()
