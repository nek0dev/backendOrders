from core.models import db_driver
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.models import Orders, State
from .schemas import Order, DroneLink, DroneIdent
from .controllers.weather import inspect_weather
from fastapi import Response, status


async def create_order(session: AsyncSession, order_to_create: Order):
    order = Orders(**order_to_create.model_dump())
    
    #block of conditional checks for starting travel
    weather = inspect_weather(latitude=str(order.latitude), longitude=str(order.longitude))

    if weather == False:
        return Response(status_code=status.HTTP_406_NOT_ACCEPTABLE)
    
    session.add(order)
    await session.commit()
    return order


async def delete_order(session: AsyncSession, order_to_delete: DroneLink):
    state = await session.execute(select(State).where(State.serial_number == order_to_delete.drone_serial))
    state = state.scalar()

    if not state:
        return Response(status_code=status.HTTP_418_IM_A_TEAPOT)

    state.state = "in base"
    state.order_id = None
    await session.commit()

    state = await session.execute(select(Orders).where(Orders.id == order_to_delete.order_id))
    state = state.scalar()
    await session.delete(state)
    await session.commit()

    return Response(status_code=status.HTTP_200_OK)


async def push_to_dron_state(session: AsyncSession, order_to_push: DroneLink):
    state = await session.execute(select(State).where(State.serial_number == order_to_push.drone_serial))
    state = state.scalar()

    if not state:
        return Response(status_code=status.HTTP_418_IM_A_TEAPOT)

    state.state = "in delivery"
    state.order_id = order_to_push.order_id
    await session.commit()

    return Response(status_code=status.HTTP_200_OK)
    

async def get_all_orders(session: AsyncSession)->list[Orders]:
    stmt = select(Orders)
    result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)