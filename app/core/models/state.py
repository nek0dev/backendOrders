from sqlalchemy import Column, String, Integer, ForeignKey, Numeric
from .base import BaseTable
from .order import Orders
from .drone import Drones


class State(BaseTable):
    id = Column(Integer, primary_key=True, autoincrement=True)
    serial_number = Column(String, ForeignKey('drones.serial_number', ondelete="cascade"), nullable=False)
    order_id = Column(Integer, ForeignKey(Orders.id))
    state = Column(String, nullable=False)
    latitude = Column(Numeric(8, 6), nullable=False)
    longitude = Column(Numeric(8, 6), nullable=False)

