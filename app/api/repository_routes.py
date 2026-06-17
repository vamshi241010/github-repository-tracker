from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.exceptions import (
    RepositoryNotFoundException,
    RepositoryAlreadyExistsException,
    GitHubRepositoryNotFoundException
)
from app.db.session import get_db
from app.schemas.repository import (
    RepositoryCreate,
    RepositoryResponse
)
from app.services.repository_service import RepositoryService

router = APIRouter(
    prefix="/repositories",
    tags=["Repositories"]
)

service = RepositoryService()


@router.post(
    "",
    response_model=RepositoryResponse,
    status_code=201
)
async def create_repository(
    payload: RepositoryCreate,
    db: AsyncSession = Depends(get_db)
):

    try:

        repository = await service.create_repository(
            payload.url,
            db
        )

        return repository

    except RepositoryAlreadyExistsException:

        raise HTTPException(
            status_code=409,
            detail="Repository already exists"
        )

    except GitHubRepositoryNotFoundException:

        raise HTTPException(
            status_code=404,
            detail="GitHub repository not found"
        )

@router.get(
    "/{repository_id}",
    response_model=RepositoryResponse
)
async def get_repository(
    repository_id: int,
    db: AsyncSession = Depends(get_db)
):

    try:

        repository = await service.get_repository(
            repository_id,
            db
        )

        return repository

    except RepositoryNotFoundException:

        raise HTTPException(
            status_code=404,
            detail="Repository not found"
        )

@router.delete(
    "/{repository_id}",
    status_code=204
)
async def delete_repository(
    repository_id: int,
    db: AsyncSession = Depends(get_db)
):
    try:
        await service.delete_repository(
            repository_id,
            db
        )

    except RepositoryNotFoundException:
        raise HTTPException(
            status_code=404,
            detail="Repository not found"
        )

@router.put(
    "/{repository_id}",
    response_model=RepositoryResponse
)
async def refresh_repository(
    repository_id: int,
    db: AsyncSession = Depends(get_db)
):
    try:

        repository = await service.refresh_repository(
            repository_id,
            db
        )

        return repository

    except RepositoryNotFoundException:

        raise HTTPException(
            status_code=404,
            detail="Repository not found"
        )

    except GitHubRepositoryNotFoundException:

        raise HTTPException(
            status_code=404,
            detail="GitHub repository not found"
        )

@router.get(
    "",
    response_model=List[RepositoryResponse]
)
async def get_all_repositories(
    page: int = 1,
    size: int = 10,
    db: AsyncSession = Depends(get_db)
):

    repositories = await service.get_paginated_repositories(
        page,
        size,
        db
    )

    return repositories