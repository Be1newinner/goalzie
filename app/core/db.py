# app/core/db.py
from __future__ import annotations
import os
from typing import AsyncGenerator
from .models import Base

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql+asyncpg://admin:admin123@localhost:5432/taskapi"
)

engine: AsyncEngine | None = None
SessionLocal: async_sessionmaker[AsyncSession] | None = None


def init_engine() -> None | AsyncEngine:
    global engine, SessionLocal
    if DATABASE_URL is None:
        raise RuntimeError("DATABASE_URL not set")
    if engine is None:
        engine = create_async_engine(
            DATABASE_URL,
            echo=False,
            pool_pre_ping=True,
        )
        SessionLocal = async_sessionmaker(
            engine, expire_on_commit=False, autoflush=False
        )
    return engine


async def create_all(engine: AsyncEngine) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("tables init success if not existed!")


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    if SessionLocal is None:
        raise RuntimeError("DB not initialized")
    session = SessionLocal()
    try:
        yield session
    finally:
        await session.close()
