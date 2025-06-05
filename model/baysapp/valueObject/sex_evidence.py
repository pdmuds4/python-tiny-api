from pydantic import field_validator

from ..._abstruct import ValueObjectModel
from ..._error import ValueObjectError


class SexEvidence(ValueObjectModel):
    value: int

    @field_validator("value")
    def check_value(cls, v):
        if v < 0 or v > 1:
            raise ValueObjectError("範囲外の性別を検出しました。0か1の整数値を入力してください。")
        return v