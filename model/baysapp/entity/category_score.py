from ..._abstruct import EntityModel
from ..valueObject import Score

class CategoryScoreEntity(EntityModel):
    entertainment: Score
    sns: Score
    game: Score
    utility: Score
    creativity: Score
    work: Score
    shopping: Score
    travel: Score
    reading: Score
    study: Score