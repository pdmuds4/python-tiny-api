from pydantic import field_validator
from typing import Literal

from ..._abstruct import ValueObjectModel
from ..._error import ValueObjectError


class PredictTypes(ValueObjectModel):
    value: Literal["category", "sex", "time", "use_time"]

    @field_validator("value")
    def check_value(cls, v):
        if v not in ["category", "sex", "time", "use_time"]:
            raise ValueObjectError("無効な予測タイプが指定されました。'category', 'sex', 'time', 'use_time' のいずれかを指定してください。")
        return v