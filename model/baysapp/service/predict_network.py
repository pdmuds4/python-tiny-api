import numpy as np
from pgmpy.inference import VariableElimination

from ..._abstruct import ServiceModel
from ..._error import ServiceError
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

        try:
            result = self.client.query([predict_type.value], evidence_dict).values
        except Exception as e:
            raise ServiceError(
                message="pgmpy.inference.VariableEliminationの実行中にエラーが発生しました",
                detail=str(e),
                status_code=500
            )
        return [Score(value=v) for v in result]
