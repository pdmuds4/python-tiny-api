from pydantic import field_validator

from ..._abstruct import ValueObjectModel
from ..._error import ValueObjectError


class CategoryEvidence(ValueObjectModel):
    value: int

    @field_validator("value")
    def check_value(cls, v):
        if v < 0 or v > 9:
            raise ValueObjectError("範囲外のカテゴリーを検出しました。0~9の整数値を入力してください。")