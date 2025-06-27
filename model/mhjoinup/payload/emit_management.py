from pydantic import BaseModel
from ..entity import *


class EmitManagementPayload(BaseModel):
    joiner: list[ManageInstantEntityTypes]
    waiter: list[ManageInstantEntityTypes]