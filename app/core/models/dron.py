from sqlalchemy import Column, Integer, Numeric, String, ARRAY
from .base import BaseTable


class Drons(BaseTable):
    serial_number = Column(String, primary_key=True)
    max_weight = Column(Numeric(2, 2), nullable=False)
    dimensions = Column(ARRAY(Integer), nullable=False)
    product_dimensions = Column(ARRAY(Integer), nullable=False)
    max_distance = Column(Integer, nullable=False)
