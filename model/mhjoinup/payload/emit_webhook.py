from pydantic import BaseModel
from ..entity import *


class EmitWebhookRequestPayload(BaseModel):
    videoId: str
    chatMessages: list[ChatMessageEntityTypes]


class EmitWebhookResponsePayload(BaseModel):
    youtube_id: str
    chat_data: list[ChatDataEntityTypes]