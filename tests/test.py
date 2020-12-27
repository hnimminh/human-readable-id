from hrid import HRID

x = HRID(':', ('codec', 'adjective', 'noun', 'verb', 'adverb'))
print(x.generate())