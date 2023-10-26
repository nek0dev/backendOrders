from sqlalchemy import Column, String, Integer, ForeignKey, Numeric
from .base import BaseTable
from .drone import Drones


class Incidents(BaseTable):
    id = Column(Integer, primary_key=True, autoincrement=True)
    serial_number = Column(String, ForeignKey(Drones.serial_number, ondelete="cascade"), nullable=False)
    text = Column(String, nullable=False)