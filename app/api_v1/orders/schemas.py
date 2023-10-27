from pydantic import BaseModel
from pydantic.types import Decimal


class Order(BaseModel):
    dimensions: list[int]
    weight: int
    latitude: Decimal
    longitude: Decimal


class DroneLink(BaseModel):
    drone_serial: str
    order_id: int

