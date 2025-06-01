from ..._abstruct import EntityModel
from ...baysapp.valueObject import Word, Appearance

class WordEntity(EntityModel):
    word: Word
    weather: Appearance
    life: Appearance
    sports: Appearance
    culture: Appearance
    economy: Appearance