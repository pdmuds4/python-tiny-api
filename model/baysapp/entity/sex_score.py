from ..._abstruct import EntityModel
from ..valueObject import Score

class SexScoreEntity(EntityModel):
    male: Score
    femail: Score