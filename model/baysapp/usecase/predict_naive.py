import numpy as np
from typing import get_args

from ..._abstruct.usecase import UseCaseModel

from ..valueObject import NewsCategories, Score, Word
from ..dto import PredictNaiveResponseDTO
from ..repository import WordsRepository

class PredictNaiveUseCase(UseCaseModel):
    repository: WordsRepository

    def __init__(self, 
        repository: WordsRepository,
        request: list[Word]
    ):
        self.repository = repository
        self.request = request

    
    def execute(self) -> PredictNaiveResponseDTO:
        categories = [NewsCategories(value=c) for c in get_args(NewsCategories.model_fields['value'].annotation)]

        scores = [
            np.log(
                np.prod([score.value for score in
                    [
                        self.repository.get_news_category_score(word, category)
                        for word in self.request
                    ]
                ])
            ) for category in categories
        ]

        scores = [score - min(scores) for score in scores]
        normalized_scores = [score / sum(scores) for score in scores]

        return PredictNaiveResponseDTO(
            weather=Score(value=normalized_scores[0]),
            life   =Score(value=normalized_scores[1]),
            sports =Score(value=normalized_scores[2]),
            culture=Score(value=normalized_scores[3]),
            economy=Score(value=normalized_scores[4])
        )
