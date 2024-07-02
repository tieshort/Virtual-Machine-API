from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

# engine = create_async_engine(DATABASE_URL)
# async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with get_async_session_maker()() as session:
        yield session


def get_engine() -> AsyncEngine:
    if "engine" not in globals():
        DATABASE_URL = (
            f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )
        globals()["engine"] = create_async_engine(DATABASE_URL)

    return globals()["engine"]


def get_async_session_maker() -> sessionmaker:
    if "async_session_maker" not in globals():
        globals()["async_session_maker"] = sessionmaker(
            get_engine(), class_=AsyncSession, expire_on_commit=False
        )

    return globals()["async_session_maker"]
