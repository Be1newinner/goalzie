# app/main.py
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from .graphql.router import graphql_router
from .core.db import init_engine, create_all


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = init_engine()
    if engine is not None:
        await create_all(engine)
    else:
        print("Some issue while starting the engine!")
    yield
    if engine is not None:
        await engine.dispose()


app = FastAPI(title="Task Manager API", lifespan=lifespan)
app.include_router(graphql_router, prefix="/graphql")


@app.middleware("http")
async def db_session_cleanup(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    finally:
        session = getattr(request.state, "db", None)
        if session is not None:
            await session.close()
            request.state.db = None


@app.get("/health")
async def health():
    return {"status": "ok"}
