from pydantic import BaseModel
from pydantic.types import Decimal


class Order(BaseModel):
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

