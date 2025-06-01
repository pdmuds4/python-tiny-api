from pydantic import BaseModel, ConfigDict

class EntityModel(BaseModel):
    model_config = ConfigDict(extra="forbid")