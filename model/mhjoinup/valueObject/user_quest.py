from pydantic import field_validator

from ..._abstruct import ValueObjectModel
from ..._error import ValueObjectError


class UserQuest(ValueObjectModel):
    value: int

    @field_validator("value")
    def check_value(cls, v):
        if v < 0: raise ValueObjectError("UserQuestは0以上の整数値です")
        return v