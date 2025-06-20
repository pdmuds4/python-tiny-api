from ..._abstruct import UseCaseModel
from ..dto import *


class EmitWebhookUseCase(UseCaseModel):
    request: EmitWebhookRequestDTO
    
    def __init__(self, request: EmitWebhookRequestDTO):
        self.request = request

    
    def execute(self) -> EmitWebhookResponseDTO:
        chat_data = [
            ChatDataEntity(
                message=message.displayMessage,
                name=message.displayName,
                avatar=message.photoUrl
            ) for message in self.request.chatMessages
        ]
        
        return EmitWebhookResponseDTO(
            youtube_id=self.request.videoId,
            chat_data=chat_data
        )