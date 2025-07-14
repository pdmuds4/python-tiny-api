from typing import Literal

ERROR_LEVELS = Literal["ValueObject", "Entity", "Repository", "Service", "UseCase", "Client"]

class BaseError(Exception):
    def __init__(self, message: str, detail: str, level: ERROR_LEVELS, status_code: int = 500):
        super().__init__(message)
        self.message = message
        self.detail = detail
        self.level = level
        self.status_code = status_code