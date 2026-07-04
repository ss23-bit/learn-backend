from __future__ import annotations
from sqlalchemy.orm import Mapped, mapped_column, relationship 
from app.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .posts import Posts

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(unique=True, nullable=False)

    password: Mapped[str] = mapped_column(unique=True, nullable=False)

    posts: Mapped[list[Posts]] = relationship(
        back_populates="users"
    )

    