from sqlalchemy import Column, Integer, ARRAY, Numeric
from .base import BaseTable


class Orders(BaseTable):
    id = Column(Integer, primary_key=True, autoincrement=True)
    dimensions = Column(ARRAY(Integer), nullable=False)
    weight = Column(Integer, nullable=False)
    latitude = Column(Numeric(8, 6), nullable=False)
    longitude = Column(Numeric(8, 6), nullable=False)