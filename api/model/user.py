
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from model.model import Base
from model.prediction import Prediction


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    room_id = Column(String(25), ForeignKey('room.name'), nullable=False)
    name = Column(String(25), nullable=False)
    predictions_json = Column(String(5000), nullable=False)
    date = Column(DateTime, onupdate=datetime.now)

    @property
    def json(self):
        return {'name': self.name, 'id': self.id, 'predictions': self.predictions_json}

    @property
    def predictions(self):
        return Prediction(self.predictions_json)
