import strawberry
from strawberry.types import Info
from typing import List, Optional

from app.core.models import User, Todo
from app.users.types import UserType
from app.users.inputs import RegisterInput, LoginInput
from app.todos.types import TodoType
from app.todos.inputs import CreateTodoInput, UpdateTodoInput

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession


async def get_db_session(info: Info) -> AsyncSession:
    return info.context["db"]


@strawberry.type
class Query:
    @strawberry.field
    async def list_todos(self, info: Info) -> List[TodoType]:
        session = await get_db_session(info)
        res = await session.execute(select(Todo).order_by(Todo.created_at.desc()))
        rows = res.scalars().all()
        return [
            TodoType(
                id=t.id,
                title=t.title,
                description=t.description,
                status=t.status,
                priority=t.priority,
                created_at=t.created_at,
                updated_at=t.updated_at,
                owner_id=t.owner_id,
            )
            for t in rows
        ]

    @strawberry.field
    async def todo(self, info: Info, id: int) -> Optional[TodoType]:
        session = await get_db_session(info)
        res = await session.execute(select(Todo).where(Todo.id == id))
        t = res.scalar_one_or_none()
        if not t:
            return None
        return TodoType(
            id=t.id,
            title=t.title,
            description=t.description,
            status=t.status,
            priority=t.priority,
            created_at=t.created_at,
            updated_at=t.updated_at,
            owner_id=t.owner_id,
        )


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def register(self, info: Info, data: RegisterInput) -> UserType:
        session = await get_db_session(info)
        user = User(
            email=data.email,
            username=data.username,
            password_hash=data.password, 
            name=data.name,
            gender=data.gender,
            dob=data.dob,
            phone=data.phone,
        )
        session.add(user)
        await session.flush()
        await session.commit()
        return UserType(
            id=user.id,
            email=user.email,
            username=user.username,
            name=user.name,
            gender=user.gender,
            dob=user.dob,
            phone=user.phone,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    @strawberry.mutation
    async def create_todo(self, info: Info, data: CreateTodoInput) -> TodoType:
        session = await get_db_session(info)
        todo = Todo(
            title=data.title,
            description=data.description,
            status=data.status,
            priority=data.priority,
            owner_id=1,  
        )
        session.add(todo)
        await session.flush()
        await session.commit()
        return TodoType(
            id=todo.id,
            title=todo.title,
            description=todo.description,
            status=todo.status,
            priority=todo.priority,
            created_at=todo.created_at,
            updated_at=todo.updated_at,
            owner_id=todo.owner_id,
        )

    @strawberry.mutation
    async def update_todo(
        self, info: Info, data: UpdateTodoInput
    ) -> Optional[TodoType]:
        session = await get_db_session(info)
        res = await session.execute(select(Todo).where(Todo.id == data.id))
        todo = res.scalar_one_or_none()
        if not todo:
            return None
        if data.title is not None:
            todo.title = data.title
        if data.description is not None:
            todo.description = data.description
        if data.status is not None:
            todo.status = data.status
        if data.priority is not None:
            todo.priority = data.priority
        await session.flush()
        await session.commit()
        return TodoType(
            id=todo.id,
            title=todo.title,
            description=todo.description,
            status=todo.status,
            priority=todo.priority,
            created_at=todo.created_at,
            updated_at=todo.updated_at,
            owner_id=todo.owner_id,
        )

    @strawberry.mutation
    async def delete_todo(self, info: Info, id: int) -> bool:
        session = await get_db_session(info)
        res = await session.execute(select(Todo).where(Todo.id == id))
        todo = res.scalar_one_or_none()
        if not todo:
            return False
        await session.delete(todo)
        await session.commit()
        return True


schema = strawberry.Schema(query=Query, mutation=Mutation)
