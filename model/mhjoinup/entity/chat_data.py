from ..._abstruct import EntityModel
from ..valueObject import *


class ChatDataEntity(EntityModel):
    message: Message
    name: UserName
    avatar: UserAvatar
    channel_id: ChannelId


class ChatDataEntityTypes(EntityModel):
    message: str
    name: str
    avatar: str
    channel_id: str