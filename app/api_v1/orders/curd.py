from core.models import db_driver
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Orders
from .schemas import Order


async def create_product(session: AsyncSession, order_to_create: Order):
    order = Orders(**order_to_create.model_dump())
    session.add(order)
    await session.commit()
    return order