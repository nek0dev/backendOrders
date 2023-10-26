from sqlalchemy import Column, String, Integer, ForeignKey, Numeric
from .base import BaseTable
from .dron import Drons


class Incidents(BaseTable):
    id = Column(Integer, primary_key=True, autoincrement=True)
    serial_number = Column(String, ForeignKey(Drons.serial_number, ondelete="cascade"), nullable=False)
    text = Column(String, nullable=False)