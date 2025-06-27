from ..._abstruct import EntityModel
from ..valueObject import *
from ..entity import *


class EmitManagementDTO(EntityModel):
    user_id: UserId
    joiner: list[ManageInstantEntity]
    waiter: list[ManageInstantEntity]
