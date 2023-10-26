from fastapi import APIRouter, Depends, status
from core.models import db_driver
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import Order
from . import curd

router = APIRouter()


@router.post("/create_order", response_model=Order, status_code=status.HTTP_201_CREATED)
async def create_order(order_to_create: Order, session: AsyncSession = Depends(db_driver.get_scoped_session)):
    return await  curd.create_product(session=session, order_to_create=order_to_create)

