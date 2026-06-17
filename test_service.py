import asyncio

from app.db.session import AsyncSessionLocal
from app.services.repository_service import RepositoryService


async def main():

    service = RepositoryService()

    async with AsyncSessionLocal() as db:

        repo = await service.create_repository(
            "https://github.com/fastapi/fastapi",
            db
        )

        print(repo.id)
        print(repo.full_name)


asyncio.run(main())