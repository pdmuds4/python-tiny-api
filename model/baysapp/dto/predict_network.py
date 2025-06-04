from typing import Union

from ..._abstruct import EntityModel
from ..valueObject import PredictTypes
from ..entity import EvidenceEntity, CategoryScoreEntity, SexScoreEntity, TimeScoreEntity, UseTimeScoreEntity


class PredictNetworkRequestDTO(EntityModel):
    type: PredictTypes
    evidence: EvidenceEntity


class PredictNetworkResponseDTO(EntityModel):
    type: PredictTypes
    score: Union[CategoryScoreEntity, SexScoreEntity, TimeScoreEntity, UseTimeScoreEntity]