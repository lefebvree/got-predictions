
from sqlalchemy import Column, Integer, String, orm

from model.model import Base


class Room(Base):
    __tablename__ = 'room'

    name = Column(String(50), primary_key=True, nullable=False, unique=True)
    users = orm.relationship('User', backref='room', lazy=True)

    @property
    def json(self):
        return {'name': self.name}
