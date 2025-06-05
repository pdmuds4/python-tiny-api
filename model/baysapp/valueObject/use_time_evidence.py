from pydantic import field_validator

from ..._abstruct import ValueObjectModel
from ..._error import ValueObjectError


class UseTimeEvidence(ValueObjectModel):
    value: int

    @field_validator("value")
    def check_value(cls, v):
        if v < 0 or v > 3:
            raise ValueObjectError("範囲外の使用時間帯を検出しました。0~3の整数値を入力してください。")
        return v