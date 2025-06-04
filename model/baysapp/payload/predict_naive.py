from pydantic import BaseModel

class PredictNaiveRequestPayload(BaseModel):
    sentence: str


class PredictNaiveResponsePayload(BaseModel):
    weather: float
    life: float
    sports: float
    culture: float
    economy: float