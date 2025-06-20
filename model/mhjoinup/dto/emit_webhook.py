from ..._abstruct import EntityModel
from ..valueObject import *
from ..entity import *


class EmitWebhookRequestDTO(EntityModel):
    videoId: YoutubeId
    chatMessages: list[ChatMessageEntity]


class EmitWebhookResponseDTO(EntityModel):
    youtube_id: YoutubeId
    chat_data: list[ChatDataEntity]