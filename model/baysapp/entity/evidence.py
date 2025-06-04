from typing import Optional

from ..._abstruct import EntityModel
from ..valueObject import CategoryEvidence, SexEvidence, TimeEvidence, UseTimeEvidence


class EvidenceEntity(EntityModel):
    category: Optional[CategoryEvidence]
    sex: Optional[SexEvidence]
    time: Optional[TimeEvidence]
    use_time: Optional[UseTimeEvidence]