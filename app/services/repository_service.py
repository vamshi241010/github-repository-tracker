from sqlalchemy.ext.asyncio import AsyncSession
from app.core.exceptions import (
    RepositoryNotFoundException,
    RepositoryAlreadyExistsException,
    GitHubRepositoryNotFoundException
)
from app.models.repository import Repository
from app.repositories.repository_repository import RepositoryRepository
from app.services.github_service import GitHubService


class RepositoryService:

    def __init__(self):
        self.github_service = GitHubService()
        self.repository_repository = RepositoryRepository()

    async def create_repository(
        self,
        url: str,
        db: AsyncSession
    ):
        path = url.replace(
            "https://github.com/",
            ""
        )

        owner, repo = path.split("/")

        response = await self.github_service.fetch_repository(
            owner,
            repo
        )

        if response.status_code == 404:
            raise GitHubRepositoryNotFoundException()

        data = response.json()

        existing = await self.repository_repository.get_by_github_id(
            db,
            data["id"]
        )

        if existing:
            raise RepositoryAlreadyExistsException()

        repository = Repository(
            github_id=data["id"],
            owner=data["owner"]["login"],
            repo_name=data["name"],
            full_name=data["full_name"],
            description=data["description"],
            stars=data["stargazers_count"],
            forks=data["forks_count"],
            language=data["language"],
            html_url=data["html_url"]
        )

        db.add(repository)

        await db.commit()

        await db.refresh(repository)

        return repository

    async def get_repository(
        self,
        repository_id: int,
        db
    ):
        repository = await self.repository_repository.get_by_id(
            db,
            repository_id
        )

        if not repository:
            raise RepositoryNotFoundException()

        return repository

    async def delete_repository(
        self,
        repository_id: int,
        db: AsyncSession
    ):
        repository = await self.repository_repository.get_by_id(
            db,
            repository_id
        )

        if not repository:
            raise RepositoryNotFoundException()

        await self.repository_repository.delete(
            db,
            repository
        )

    async def refresh_repository(
        self,
        repository_id: int,
        db: AsyncSession
    ):
        repository = await self.repository_repository.get_by_id(
            db,
            repository_id
        )

        if not repository:
            raise RepositoryNotFoundException()

        response = await self.github_service.fetch_repository(
            repository.owner,
            repository.repo_name
        )
        if response.status_code == 404:
            raise GitHubRepositoryNotFoundException()

        data = response.json()

        repository.description = data["description"]
        repository.stars = data["stargazers_count"]
        repository.forks = data["forks_count"]
        repository.language = data["language"]
        repository.html_url = data["html_url"]

        repository = await self.repository_repository.update(
            db,
            repository
        )

        return repository

    async def get_all_repositories(
        self,
        db: AsyncSession
    ):
        repositories = await self.repository_repository.get_all(
            db
        )

        return repositories


    async def get_paginated_repositories(
        self,
        page: int,
        size: int,
        db: AsyncSession
    ):
        skip = (page - 1) * size

        repositories = await self.repository_repository.get_paginated(
            db,
            skip,
            size
        )

        return repositories