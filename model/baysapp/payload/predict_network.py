from pydantic import BaseModel
from typing import Literal, Optional


class EvidencePayload(BaseModel):
    category: Optional[int]
    sex: Optional[int]
    time: Optional[int]
    use_time: Optional[int]


class PredictNetworkRequestPayload(BaseModel):
    type: Literal["category", "sex", "time", "use_time"]
    evidence: EvidencePayload


class PredictNetworkResponsePayload(BaseModel):
    type: Literal["category", "sex", "time", "use_time"]
    score: dict[str, float]


