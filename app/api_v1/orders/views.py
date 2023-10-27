from fastapi import APIRouter, Depends, status
from core.models import db_driver
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import Order, DroneLink, DroneIdent
from . import curd
from core.auth.auth_bearer import JWTBearer, JWTHeader

router = APIRouter()


@router.post("/create_order", response_model=Order, status_code=status.HTTP_201_CREATED)
async def create_order(order_to_create: Order, session: AsyncSession = Depends(db_driver.get_scoped_session), token: JWTHeader = Depends(JWTBearer())):
    return await curd.create_order(session=session, order_to_create=order_to_create)#


@router.delete("/delete_order", response_model=DroneLink)
async def delete_order(order_delete: DroneLink, session: AsyncSession = Depends(db_driver.get_scoped_session), token: JWTHeader = Depends(JWTBearer())):
    return await curd.delete_order(session=session, order_to_delete=order_delete)#


@router.post("/run_order", response_model=DroneLink)
async def run_order(order_to_push: DroneLink, session: AsyncSession = Depends(db_driver.get_scoped_session), token: JWTHeader = Depends(JWTBearer())):
    return await curd.push_to_dron_state(session=session, order_to_push=order_to_push)#


@router.get("/get_all_orders", response_model=list[Order], status_code=status.HTTP_200_OK)
async def get_all_orders(session: AsyncSession = Depends(db_driver.get_scoped_session)):
    return await curd.get_all_orders(session=session)


@router.get("/get/{order_id}", status_code=status.HTTP_200_OK)
async def get_order_by_id(order_id: str, session: AsyncSession = Depends(db_driver.get_scoped_session)):
    return await curd.get_order_by_id(order_id=order_id, session=session)
