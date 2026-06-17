import asyncio

from app.db.database import engine
from app.models.base import Base

# VERY IMPORTANT
from app.models.repository import Repository


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print("Tables created successfully")


asyncio.run(main())