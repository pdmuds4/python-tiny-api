from pydantic import BaseModel, ConfigDict

class RepositoryModel(BaseModel):
    model_config = ConfigDict(extra="forbid", arbitrary_types_allowed=True)