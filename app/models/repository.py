from datetime import datetime

from sqlalchemy import Integer, String, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base

class Repository(Base):
    __tablename__ = "repositories"

    id:Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    github_id:Mapped[int] = mapped_column(
        Integer,
        unique=True,
        nullable=False
    )
    owner:Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    repo_name:Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    full_name: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    stars: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    forks: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    language: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    html_url: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )