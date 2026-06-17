import asyncio

from app.services.github_service import GitHubService


async def main():
    service = GitHubService()

    response = await service.fetch_repository(
        "fastapi",
        "fastapi"
    )

    print(response.status_code)

    data = response.json()

    print(data["full_name"])


asyncio.run(main())