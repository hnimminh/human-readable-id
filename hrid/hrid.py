import random
from .adjectives import ADJECTIVES
from .nouns import NOUNS, ANIMALS, FLOWERS
from .verbs import VERBS
from .adverbs import ADVERBS


DICTIONARY = {
    'adjective': ADJECTIVES,
    'noun': NOUNS,
    'verb': VERBS,
    'adverb': ADVERBS,
    'number': list(map(str, range(10,99)))
}


class HRID:
    def __init__(self, delimeter='-', hridfmt=('adjective', 'noun', 'verb', 'adverb')):
        self.delimeter = delimeter
        self.phrasefmt = list()
        for element in hridfmt:
            self.phrasefmt.append(DICTIONARY.get(element, element))

    def generate(self):
        phrases = list()
        for element in self.phrasefmt:
            if isinstance(element, (str)): 
                phrases.append(element)
            if isinstance(element, (list)):
                phrases.append(random.choice(element))

        return self.delimeter.join(phrases)
