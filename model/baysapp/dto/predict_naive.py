from ..._abstruct import EntityModel
from ...baysapp.valueObject import Sentence, Score


class PredictNaiveRequestModel(EntityModel):
    sentence: str


class PredictNaiveResponseModel(EntityModel):
    weather: float
    life: float
    sports: float
    culture: float
    economy: float


class PredictNaiveRequestDTO(EntityModel):
    sentence: Sentence


class PredictNaiveResponseDTO(EntityModel):
    weather: Score
    life: Score
    sports: Score
    culture: Score
    economy: Score