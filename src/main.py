from fastapi import FastAPI
from fastapi.responses import JSONResponse

from order.router import router as order_router
from order.models import Base
from database import engine

import uvicorn
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

    await engine.dispose()
    print("Application shutdown complete")


app = FastAPI(lifespan=lifespan)

app.include_router(order_router)
app.include_router(email_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
