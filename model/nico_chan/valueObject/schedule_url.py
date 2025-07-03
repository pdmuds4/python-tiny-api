from urllib.parse import urlparse
from pydantic import field_validator

from ..._abstruct import ValueObjectModel
from ..._error import ValueObjectError


class ScheduleURL(ValueObjectModel):
    value: str

    @field_validator("value")
    def check_value(cls, v):
        parsed_url = urlparse(v)
        if not all([parsed_url.scheme in ("http", "https"), parsed_url.netloc]):
            raise ValueObjectError("ScheduleURLは有効なURLではありません。")
        return v