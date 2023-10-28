from pydantic import BaseModel
from pydantic.types import Decimal
from typing import Optional


class Order(BaseModel):
    dimensions: list[int]
    weight: int
    latitude: Decimal
    longitude: Decimal


class OrderWithID(BaseModel):
    id: int
    dimensions: list[int]
    weight: int
    latitude: Decimal
    longitude: Decimal


class DroneIdent(BaseModel):
    drone_serial: str


class DroneLink(DroneIdent):
    drone_serial: str
    order_id: int

