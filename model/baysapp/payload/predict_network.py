from pydantic import BaseModel
from typing import Literal, Optional


class PredictNetworkRequestPayload(BaseModel):
    type: Literal["category", "sex", "time", "use_time"]
    evidence: dict[str, Optional[str]]


class PredictNetworkResponsePayload(BaseModel):
    type: Literal["category", "sex", "time", "use_time"]
    score: dict[str, float]


