from contextlib import asynccontextmanager
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from core.models import db_driver, BaseTable


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_driver.engine.begin() as conn:
        await conn.run_sync(BaseTable.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST, GET, DELETE"],
    allow_headers=["*"]
)


@app.get("/")
def index():
    return Response(status_code=status.HTTP_200_OK)