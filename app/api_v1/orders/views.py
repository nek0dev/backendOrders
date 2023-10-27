from fastapi import APIRouter, Depends, status
from core.models import db_driver
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import Order, DroneLink
from . import curd


router = APIRouter()


@router.post("/create_order", response_model=Order, status_code=status.HTTP_201_CREATED)
async def create_order(order_to_create: Order, session: AsyncSession = Depends(db_driver.get_scoped_session)):
    return await curd.create_order(session=session, order_to_create=order_to_create)


@router.delete("/delete_order", response_model=DroneLink)
async def delete_order(order_delete: DroneLink, session: AsyncSession = Depends(db_driver.get_scoped_session)):
    return await curd.delete_order(session=session, order_to_delete=order_delete)


@router.post("/run_order", response_model=DroneLink)
async def run_order(order_to_push: DroneLink, session: AsyncSession = Depends(db_driver.get_scoped_session)):
    return await curd.push_to_dron_state(session=session, order_to_push=order_to_push)