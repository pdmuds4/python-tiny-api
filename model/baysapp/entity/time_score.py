from ..._abstruct import EntityModel
from ..valueObject import Score

class TimeScoreEntity(EntityModel):
    morning: Score # 3~9 clock
    afternoon: Score # 9~15 clock
    evening: Score # 15~21 clock
    night: Score # 21~3 clock