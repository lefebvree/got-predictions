
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum, PickleType, orm

from model.model import Base
from model.prediction_choices import Choice


class Prediction(Base):
    __tablename__ = 'prediction'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = orm.relationship("User", uselist=False, back_populates="user")

    predictions = Column(PickleType, nullable=False)
