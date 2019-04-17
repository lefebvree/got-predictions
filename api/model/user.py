
from sqlalchemy import Column, Integer, String, ForeignKey, orm

from model.model import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey('room.id'), nullable=False)
    name = Column(String(25), nullable=False, unique=True)
    orm.relationship("Prediction", uselist=False, back_populates="prediction")

    @property
    def json(self):
        return {'name': self.name, 'id': self.id}
