import strawberry
from typing import Optional

@strawberry.input
class CreateTodoInput:
    title: str
    description: Optional[str] = None
    status: str = "PENDING"
    priority: str = "MEDIUM"

@strawberry.input
class UpdateTodoInput:
    id: int
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
