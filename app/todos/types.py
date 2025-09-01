import strawberry
from datetime import datetime
from typing import Optional


@strawberry.type
class TodoType:
    id: int
    title: str
    description: Optional[str]
    status: str
    priority: str
    created_at: datetime
    updated_at: datetime
    owner_id: int
