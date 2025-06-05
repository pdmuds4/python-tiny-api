from pydantic import field_validator
from typing import Literal

from ..._abstruct import ValueObjectModel
from ..._error import ValueObjectError

class NewsCategories(ValueObjectModel):
    value: Literal["weather", "life", "sports", "culture", "economy"]

    @field_validator("value")
    def check_value(cls, v):
        if v not in ["weather", "life", "sports", "culture", "economy"]:
            raise ValueObjectError("無効なニュースカテゴリが指定されました。'weather', 'life', 'sports', 'culture', 'economy' のいずれかを指定してください。")
        return v
