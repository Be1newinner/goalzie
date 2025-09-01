import strawberry
from typing import Optional
from datetime import date


@strawberry.input
class RegisterInput:
    email: str
    username: str
    password: str
    name: Optional[str] = None
    gender: Optional[str] = None
    dob: Optional[date] = None
    phone: Optional[str] = None


@strawberry.input
class LoginInput:
    email: str
    password: str
