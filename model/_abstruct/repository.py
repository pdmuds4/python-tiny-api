from pydantic import BaseModel, ConfigDict

class RepositoryModel(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")