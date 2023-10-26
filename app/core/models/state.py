from sqlalchemy import Column, String, Integer, ForeignKey, Numeric
from .base import BaseTable
from .order import Orders
from .dron import Drons


class State(BaseTable):
    id = Column(Integer, primary_key=True, autoincrement=True)
    serial_number = Column(String, ForeignKey(Drons.serial_number))
    order_id = Column(Integer, ForeignKey(Orders.id))
    state = Column(String, nullable=False)
    latitude = Column(Numeric(2, 6), nullable=False)
    longitude = Column(Numeric(2, 6), nullable=False)

