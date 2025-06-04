from ..._abstruct import UseCaseModel
from ..service import ParseWordsService, PredictNaiveService
from ..dto import PredictNaiveRequestDTO, PredictNaiveResponseDTO


class PredictNaiveUseCase(UseCaseModel):
    request: PredictNaiveRequestDTO
    parseWordsService: ParseWordsService
    predictNaiveService: PredictNaiveService

    def __init__(self, 
        request: PredictNaiveRequestDTO, 
        parseWordsService: ParseWordsService,
        predictNaiveService: PredictNaiveService
    ):
        self.request = request
        self.parseWordsService = parseWordsService
        self.predictNaiveService = predictNaiveService


    def execute(self) -> PredictNaiveResponseDTO:
        sentence = self.request.sentence
        words = self.parseWordsService.execute(sentence)
        scores = self.predictNaiveService.execute(words)

        return PredictNaiveResponseDTO(
            weather=scores[0],
            life=scores[1],
            sports=scores[2],
            culture=scores[3],
            economy=scores[4]
        )