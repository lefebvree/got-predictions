
from sqlalchemy import Column, Integer, String, orm

from model.model import Base


class Room(Base):
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    users = orm.relationship('User', backref='room', lazy=True)

    @property
    def json(self):
        return {'name': self.name, 'id': self.id}
