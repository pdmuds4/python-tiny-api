from ..._abstruct import EntityModel
from ..valueObject import *


class ChatMessageEntity(EntityModel):
    displayMessage: Message
    displayName: UserName
    photoUrl: UserAvatar
