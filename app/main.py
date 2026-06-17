from fastapi import FastAPI

from app.api.repository_routes import router


app = FastAPI(
    title="GitHub Repository Tracker"
)

app.include_router(router)


@app.get("/")
async def root():
    return {
        "message": "API Running"
    }