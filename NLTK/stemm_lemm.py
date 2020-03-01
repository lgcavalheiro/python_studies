import nltk
import numpy
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag

raw = """Call me Ishmael. Some years ago nevermind how long precisely having
        ... little or no money in my purse, and nothing particular to interest me on shore
        ... I thought i would sail about a little and see the watery part of the world."""

tokens = nltk.word_tokenize(raw)

porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()

p_res = [porter.stem(t) for t in tokens]
l_res = [lancaster.stem(t) for t in tokens]

wnl = nltk.WordNetLemmatizer()

wnl_res = [wnl.lemmatize(t) for t in tokens]
