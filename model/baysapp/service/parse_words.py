from MeCab import Tagger

from ..._abstruct.service import ServiceModel
from ...baysapp.valueObject import Sentence, Word


class ParseWordsService(ServiceModel):
    def __init__(self, mecab_tagger: Tagger, sentence: Sentence):
        super().__init__(client=mecab_tagger, request=sentence)


    def execute(self) -> list[Word]:
        node = self.client.parseToNode(self.request.value)

        words = []
        while node:
            if node.feature.split(',')[1] in ['数詞','非自立可能','接尾']:
                node=node.next
                continue

            if node.feature.split(',')[0] in ['名詞', '動詞', '形容詞']:
                words.append(Word(value=node.surface))

            node=node.next
        
        return words
