import nltk
import numpy
from nltk.book import *
from nltk.corpus import brown, webtext, inaugural

#nltk.download('book')

print(text1)

brown.categories()
print(brown.words(categories='adventure'))

for fileid in webtext.fileids():
    print(fileid, webtext.raw(fileid)[:20], '...')

print(inaugural.fileids()[-1])