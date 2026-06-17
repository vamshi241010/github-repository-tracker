import asyncio

from app.db.database import engine


async def main():
    async with engine.begin() as conn:
        print("Database Connected Successfully")


asyncio.run(main())