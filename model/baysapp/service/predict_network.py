import numpy as np
from pgmpy.inference import VariableElimination

from ..._abstruct import ServiceModel
from ..valueObject import PredictTypes, Score
from ..entity import EvidenceEntity

class PredictNetworkService(ServiceModel):
    client: VariableElimination

    def __init__(self, client: VariableElimination):
        self.client = client


    def execute(self, predict_type: PredictTypes, evidence: EvidenceEntity) -> list[Score]:
        evidence_dump = evidence.model_dump()
        evidence_dict = {
            type: evidence['value'] for type, evidence in evidence_dump.items()
            if evidence is not None and type != predict_type.value
        }

        result = self.client.query([predict_type.value], evidence_dict).values
        return [Score(value=v) for v in result]