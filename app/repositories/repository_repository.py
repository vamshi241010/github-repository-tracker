from sqlalchemy import select,func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.repository import Repository


class RepositoryRepository:

    async def get_by_github_id(
        self,
        db: AsyncSession,
        github_id: int
    ):
        result = await db.execute(
            select(Repository).where(
                Repository.github_id == github_id
            )
        )

        return result.scalar_one_or_none()

    async def get_by_id(
        self,
        db: AsyncSession,
        repository_id: int
    ):
        result = await db.execute(
            select(Repository).where(
                Repository.id == repository_id
            )
        )

        return result.scalar_one_or_none()

    async def delete(
        self,
        db: AsyncSession,
        repository: Repository
    ):
        await db.delete(repository)
        await db.commit()

    async def update(
        self,
        db: AsyncSession,
        repository: Repository
    ):
        await db.commit()
        await db.refresh(repository)

        return repository

    async def get_all(
        self,
        db: AsyncSession
    ):
        result = await db.execute(
            select(Repository)
        )

        return result.scalars().all()

    async def get_paginated(
        self,
        db: AsyncSession,
        skip: int,
        limit: int
    ):
        result = await db.execute(
            select(Repository)
            .offset(skip)
            .limit(limit)
        )

        return result.scalars().all()

    