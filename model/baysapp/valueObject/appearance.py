from pydantic import field_validator

from ..._abstruct import ValueObjectModel
from ..._error import ValueObjectError

class Appearance(ValueObjectModel):
    value: int

    @field_validator("value")
    def check_value(cls, v):
        if v < 0: raise ValueObjectError("0未満の値が指定されました。0以上の整数を指定してください。")
        
        return v