from typing import Literal, TypedDict


class ChatRequestContract(TypedDict):
    session_id: str
    message: str


class ChatMessageContract(TypedDict):
    id: str
    role: Literal["user", "assistant", "system"]
    content: str


class ChatResponseContract(TypedDict):
    session_id: str
    reply: ChatMessageContract
    flow_state: str

