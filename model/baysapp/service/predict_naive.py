import numpy as np
from typing import get_args

from ..._abstruct import ServiceModel
from ..valueObject import NewsCategories, Score, Word
from ..repository import WordsRepository

class PredictNaiveService(ServiceModel):
    repository: WordsRepository

    def __init__(self, 
        repository: WordsRepository,
    ):
        self.repository = repository

    
    def execute(self, request: list[Word]) -> list[Score]:
        categories = [NewsCategories(value=c) for c in get_args(NewsCategories.model_fields['value'].annotation)]

        category_scores = []
        for category in categories:
            sentence_scores = []
            category_laplace_smoothing_score = self.repository.get_laplace_smoothing_score(category)
            
            for word in request:
                word_score = self.repository.get_news_category_score(word, category)
                if word_score:
                    sentence_scores.append(word_score.value)
                else:
                    sentence_scores.append(category_laplace_smoothing_score.value)
            
            category_scores.append(np.prod(sentence_scores))

        scores = np.log(category_scores)
        scores = [score - min(scores) for score in scores]
        normalized_scores = [Score(value=score / sum(scores)) for score in scores]

        return normalized_scores
