from ..._abstruct import EntityModel
from ..valueObject import *


class ManageInstantEntity(EntityModel):
    name: UserName
    avatar: UserAvatar
    quest: UserQuest


class ManageInstantEntityTypes(EntityModel):
    name: str
    avatar: str
    quest: int
