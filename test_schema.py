from app.schemas.repository import RepositoryCreate


data = RepositoryCreate(
    url="https://github.com/fastapi/fastapi"
)

print(data)