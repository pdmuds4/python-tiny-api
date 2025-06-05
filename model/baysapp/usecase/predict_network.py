from ..._abstruct import UseCaseModel
from ..._error import UseCaseError
from ..service import PredictNetworkService
from ..dto import PredictNetworkRequestDTO, PredictNetworkResponseDTO
from ..entity import CategoryScoreEntity, SexScoreEntity, TimeScoreEntity, UseTimeScoreEntity

class PredictNetworkUseCase(UseCaseModel):
    request: PredictNetworkRequestDTO
    predictNetworkService: PredictNetworkService

    def __init__(self,
        request: PredictNetworkRequestDTO,
        predictNetworkService: PredictNetworkService
    ):
        self.request = request
        self.predictNetworkService = predictNetworkService

    def execute(self) -> PredictNetworkResponseDTO:
        type = self.request.type
        evidence = self.request.evidence

        scores = self.predictNetworkService.execute(type, evidence)

        match type.value, len(scores):
            case "category", 10:
                return PredictNetworkResponseDTO(
                    type=type,
                    score=CategoryScoreEntity(
                        entertainment=scores[0],
                        sns=scores[1],
                        game=scores[2],
                        utility=scores[3],
                        creativity=scores[4],
                        work=scores[5],
                        shopping=scores[6],
                        travel=scores[7],
                        reading=scores[8],
                        study=scores[9]
                    )
                )
            case "sex", 2:
                return PredictNetworkResponseDTO(
                    type=type,
                    score=SexScoreEntity(
                        male=scores[0],
                        femail=scores[1]
                    )
                )
            case "time", 4:
                return PredictNetworkResponseDTO(
                    type=type,
                    score=TimeScoreEntity(
                        morning=scores[0],
                        afternoon=scores[1],
                        evening=scores[2],
                        night=scores[3]
                    )
                )
            case "use_time", 4:
                return PredictNetworkResponseDTO(
                    type=type,
                    score=UseTimeScoreEntity(
                        short=scores[0],
                        middle=scores[1],
                        long=scores[2],
                        verylong=scores[3]
                    )
                )
            case _:
                raise UseCaseError(
                    message="予期しない推論スコアが検出されました",
                    detail=f"Type: {type.value}, Scores: {scores}",
                    status_code=500
                )