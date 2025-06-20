import re
from pydantic import field_validator

from ..._abstruct import ValueObjectModel
from ..._error import ValueObjectError


class ChannelId(ValueObjectModel):
    value: str

    @field_validator("value")
    def check_value(cls, v):
        if len(v) != 24:                           raise ValueObjectError("ChannelIdは24文字固定長です。")
        if not re.match(r"/^[A-Za-z0-9_-]+$/", v): raise ValueObjectError("ChannelIdは半角英数字、アンダースコア、ハイフンのみ使用可能です")
        
        return v