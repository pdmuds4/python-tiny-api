from MeCab import Tagger

from ..._abstruct.usecase import UseCaseModel
from ..valueObject import Word
from ..dto import PredictNaiveRequestDTO


class ParseWordsUseCase(UseCaseModel):
    client: Tagger
    request: PredictNaiveRequestDTO

    def __init__(self, client: Tagger, request: PredictNaiveRequestDTO):
        self.client = client
        self.request = request

    def execute(self) -> list[Word]:
        node = self.client.parseToNode(self.request.sentence.value)

        words = []
        while node:
            if node.feature.split(',')[1] in ['数詞','非自立可能','接尾']:
                node=node.next
                continue

            if node.feature.split(',')[0] in ['名詞', '動詞', '形容詞']:
                words.append(Word(value=node.surface))

            node=node.next
        
        return words
