from typing import Literal, Optional

from pydantic import BaseModel, Field


ModeType = Literal["explain", "fix", "generate", "review"]


class AskRequest(BaseModel):
    mode: ModeType = Field(..., description="Режим работы ассистента")
    prompt: str = Field(..., min_length=3, description="Текстовый запрос пользователя")
    code: Optional[str] = Field(default=None, description="Фрагмент кода при необходимости")


class AskResponse(BaseModel):
    mode: ModeType
    answer: str


class HealthResponse(BaseModel):
    status: str
    provider: str
    model: str
