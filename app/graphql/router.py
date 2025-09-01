# app/graphql/router.py
from fastapi import Request, Depends
from strawberry.fastapi import GraphQLRouter
from .schema import schema
from app.core.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession


async def get_context(
    request: Request,
    db: AsyncSession = Depends(get_db),
):
    request.state.db = db
    return {"db": db, "request": request}


graphql_router = GraphQLRouter(
    schema=schema,
    context_getter=get_context,
)
