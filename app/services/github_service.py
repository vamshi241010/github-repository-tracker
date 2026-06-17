import httpx

from app.core.config import settings


class GitHubService:

    async def fetch_repository(
        self,
        owner: str,
        repo: str
    ):

        url = (
            f"{settings.GITHUB_API_BASE}"
            f"/repos/{owner}/{repo}"
        )

        headers = {}

        if settings.GITHUB_TOKEN:
            headers["Authorization"] = (
                f"Bearer {settings.GITHUB_TOKEN}"
            )

        async with httpx.AsyncClient(
            timeout=settings.REQUEST_TIMEOUT,
            follow_redirects=True
        ) as client:

            response = await client.get(
                url,
                headers=headers
            )

            return response