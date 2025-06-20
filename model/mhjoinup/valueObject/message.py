from pydantic import field_validator

from ..._abstruct import ValueObjectModel
from ..._error import ValueObjectError


class Message(ValueObjectModel):
    value: str

    @field_validator("value")
    def check_value(cls, v):
        if len(v) < 1 or len(v) > 200:
            raise ValueObjectError("Messageは1文字以上200文字以下です。")
        return v