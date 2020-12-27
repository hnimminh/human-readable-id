from hrid import HRID

hruuid = HRID()
print(hruuid.generate())

hruuid1 = HRID(':', ('codec', 'adjective', 'noun', 'verb', 'adverb'))
print(hruuid1.generate())

hruuid2 = HRID('-', ('number', 'adjective', 'noun', 'verb', 'adverb'))
print(hruuid2.generate())