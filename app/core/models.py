# app/core/models.py
from __future__ import annotations
from datetime import date, datetime
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey, func, Enum, Integer, Date, DateTime


class Base(DeclarativeBase):
    pass


# Enums for status/priority are explicit for clarity and validation
TodoStatus = Enum("PENDING", "IN_PROGRESS", "DONE", name="todo_status")
TodoPriority = Enum("LOW", "MEDIUM", "HIGH", "URGENT", name="todo_priority")


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    name: Mapped[Optional[str]] = mapped_column(String(120), default=None)
    gender: Mapped[Optional[str]] = mapped_column(String(20), default=None)
    dob: Mapped[Optional[date]]
    phone: Mapped[Optional[str]] = mapped_column(String(20), default=None)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    todos: Mapped[list["Todo"]] = relationship(
        back_populates="owner", cascade="all, delete-orphan"
    )


class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[Optional[str]] = mapped_column(Text, default=None)
    status: Mapped[str] = mapped_column(TodoStatus, default="PENDING")
    priority: Mapped[str] = mapped_column(TodoPriority, default="MEDIUM")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), index=True
    )
    owner: Mapped["User"] = relationship(back_populates="todos")
