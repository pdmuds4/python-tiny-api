from ..._abstruct import EntityModel
from ...baysapp.valueObject import Sentence, Score


class PredictNaiveRequestDTO(EntityModel):
    sentence: Sentence


class PredictNaiveResponseDTO(EntityModel):
    weather: Score
    life: Score
    sports: Score
    culture: Score
    economy: Score