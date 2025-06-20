from pydantic import field_validator

from ..._abstruct import ValueObjectModel
from ..._error import ValueObjectError


class UserName(ValueObjectModel):
    value: str

    @field_validator("value")
    def check_value(cls, v):
        if len(v) < 1: raise ValueObjectError("UserNameは1文字以上です。")
        return v