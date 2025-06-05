from pydantic import field_validator

from ..._abstruct import ValueObjectModel
from ..._error import ValueObjectError

class Score(ValueObjectModel):
    value: float

    @field_validator("value")
    def check_value(cls, v):
        if v < 0: raise ValueObjectError("0以下のスコアが検出されました。0以上1以下の値を指定してください。")
        if v > 1: raise ValueObjectError("100を超過するスコアが検出されました。0以上1以下の値を指定してください。")
        
        return v