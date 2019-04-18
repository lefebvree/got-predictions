
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from model.model import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    room_id = Column(String(50), ForeignKey('room.name'), nullable=False)
    name = Column(String(25), nullable=False, unique=True)
    predictions_json = Column(String(10), nullable=False)
    date = Column(DateTime, onupdate=datetime.now)

    @property
    def json(self):
        return {'name': self.name, 'id': self.id}
