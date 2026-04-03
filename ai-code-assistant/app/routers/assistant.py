from fastapi import APIRouter, HTTPException

from app.core.config import settings
from app.schemas import AskRequest, AskResponse, HealthResponse
from app.services.llm_client import LLMClient
from app.services.prompts import build_prompt

router = APIRouter(prefix="/assistant", tags=["assistant"])


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        provider=settings.llm_provider,
        model=settings.llm_model,
    )


@router.post("/ask", response_model=AskResponse)
async def ask_assistant(payload: AskRequest) -> AskResponse:
    client = LLMClient()
    prompt = build_prompt(payload.mode, payload.prompt, payload.code)

    try:
        answer = await client.ask(prompt)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Ошибка LLM API: {exc}") from exc

    return AskResponse(mode=payload.mode, answer=answer)
