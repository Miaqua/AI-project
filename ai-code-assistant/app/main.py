from fastapi import FastAPI

from app.core.config import settings
from app.routers.assistant import router as assistant_router

app = FastAPI(
    title=settings.app_name,
    description="MVP AI-ассистента для разработчиков",
    version="0.1.0",
)

app.include_router(assistant_router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "AI Code Assistant is running"}
