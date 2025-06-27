from pydantic import field_validator

from ..._abstruct import ValueObjectModel
from ..._error import ValueObjectError


class UserId(ValueObjectModel):
    value: str

    @field_validator("value")
    def check_value(cls, v):
        if len(v) != 64: raise ValueObjectError("UserIdは64文字固定長です")
        return v