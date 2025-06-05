from pydantic import field_validator

from ..._abstruct import ValueObjectModel
from ..._error import ValueObjectError

class Sentence(ValueObjectModel):
    value: str

    @field_validator("value")
    def check_value(cls, v):
        if len(v) == 0: raise ValueObjectError("空の文章が検出されました。空でない文章を指定してください。")
        if len(v) <= 5: raise ValueObjectError("5文字以下の文章が検出されました。5文字以上の文章を指定してください。")
        if v.isspace(): raise ValueObjectError("空白のみの文章が検出されました。空白以外の文字を含む文章を指定してください。")
        
        return v