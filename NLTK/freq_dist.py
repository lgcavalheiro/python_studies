import nltk
import numpy
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.book import *

ex = text1[:50]

fdist = FreqDist(text1)

count = len(fdist)

print(fdist.most_common(50))
