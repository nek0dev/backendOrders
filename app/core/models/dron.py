from sqlalchemy import Column, Integer, Numeric, String, ARRAY
from sqlalchemy.orm import relationship
from .base import BaseTable


class Drones(BaseTable):
    serial_number = Column(String, primary_key=True)
    max_weight = Column(Numeric(4, 2), nullable=False)
    dimensions = Column(ARRAY(Integer), nullable=False)
    product_dimensions = Column(ARRAY(Integer), nullable=False)
    max_distance = Column(Integer, nullable=False)

    state = relationship('States', backref='drons', cascade='all, delete')
    incidents = relationship('Incidents', backref='drons', cascade='all, delete')
