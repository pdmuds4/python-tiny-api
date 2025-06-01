from .abstruct import BaseError

class RepositoryError(BaseError):
    def __init__(self, message: str, detail: str, status_code: int):
        super().__init__(
            message=message, 
            detail=detail,
            level="Repository",
            status_code=status_code
        )