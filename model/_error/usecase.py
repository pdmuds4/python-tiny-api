from .abstruct import BaseError

class UseCaseError(BaseError):
    def __init__(self, message: str, detail: str, status_code: int):
        super().__init__(
            message=message, 
            detail=detail,
            level="UseCase",
            status_code=status_code
        )