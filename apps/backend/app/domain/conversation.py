from typing import Literal

from pydantic import BaseModel, Field


class ConversationMessage(BaseModel):
    id: str
    role: Literal["user", "assistant", "system"]
    content: str


class ConversationState(BaseModel):
    session_id: str
    flow_state: str = "intake"
    messages: list[ConversationMessage] = Field(default_factory=list)
