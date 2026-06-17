from pydantic import BaseModel, field_validator
from urllib.parse import urlparse
from datetime import datetime

class RepositoryCreate(BaseModel):
    url: str

    @field_validator("url")
    @classmethod
    def validate_github_url(cls, value: str):

        parsed = urlparse(value)

        if parsed.netloc != "github.com":
            raise ValueError(
                "Only GitHub repository URLs are allowed"
            )

        path_parts = parsed.path.strip("/").split("/")

        if len(path_parts) != 2:
            raise ValueError(
                "URL must be in format https://github.com/owner/repository"
            )

        return value

class RepositoryResponse(BaseModel):
    id: int
    github_id: int
    owner: str
    repo_name: str
    full_name: str
    description: str | None
    stars: int
    forks: int
    language: str | None
    html_url: str
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }