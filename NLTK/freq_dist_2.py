import nltk
import numpy
import matplotlib
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.book import text1
from nltk import FreqDist
import matplotlib.pyplot as plt

fdist = FreqDist(text1)

common = fdist.most_common(50)

plot = fdist.plot(50, cumulative=True)

print(120000/len(text1)*100)

print(fdist.hapaxes())

ex = set(text1)

big_words = [w for w in ex if len(w)>15]

print(sorted(big_words))

print(fdist['whale'])

plt.savefig("mygraph.png")