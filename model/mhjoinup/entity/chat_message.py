from pydantic import ConfigDict
from ..._abstruct import EntityModel
from ..valueObject import *


class ChatMessageEntity(EntityModel):
    displayMessage: Message
    displayName: UserName
    photoUrl: UserAvatar
    platformAudienceId: ChannelId


class ChatMessageEntityTypes(EntityModel):
    displayMessage: str
    displayName: str
    photoUrl: str
    platformAudienceId: str
    
    model_config = ConfigDict(extra="allow")