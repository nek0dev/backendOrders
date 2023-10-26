from fastapi import APIRouter
from .orders.views import router as orders_router

router = APIRouter()

router.include_router(router=orders_router, prefix="/orders")