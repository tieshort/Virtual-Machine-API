from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from database import engine
from order.models import Base

from order.router import router as order_router
from vm_panel.router import router as vm_panel_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

    await engine.dispose()
    print("Application shutdown complete")


app = FastAPI(lifespan=lifespan)

app.include_router(order_router)
app.include_router(vm_panel_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
