from .abstruct import BaseError

class ValueObjectError(BaseError):
    def __init__(self, message: str):
        super().__init__(
            message=message, 
            detail=None,
            level="ValueObject",
            status_code=422
        )