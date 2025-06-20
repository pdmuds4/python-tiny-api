from ..._abstruct import EntityModel
from ..valueObject import *


class ChatDataEntity(EntityModel):
    message: Message
    name: UserName
    avatar: UserAvatar


class ChatDataEntityTypes(EntityModel):
    message: str
    name: str
    avatar: str