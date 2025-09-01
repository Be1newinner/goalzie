import strawberry
from datetime import date, datetime
from typing import Optional


@strawberry.type
class UserType:
    id: int
    email: str
    username: str
    name: Optional[str]
    gender: Optional[str]
    dob: Optional[date]
    phone: Optional[str]
    created_at: datetime
    updated_at: datetime
