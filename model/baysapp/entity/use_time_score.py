from ..._abstruct import EntityModel
from ..valueObject import Score

class UseTimeScoreEntity(EntityModel):
    short: Score # 0~2h
    middle: Score # 2~4h
    long: Score # 4~6h
    verylong: Score # 6~8h