from pydantic import BaseModel, ConfigDict

class ValueObjectModel(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")