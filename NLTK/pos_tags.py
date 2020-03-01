import nltk
import numpy
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag

ex = 'Time to get started with natural language processing. Python makes it easy!'

sent_tokens = sent_tokenize(ex)
print(sent_tokens)

word_tokens = word_tokenize(ex)
print(word_tokens)

tags = pos_tag(word_tokens)
print(tags)

#nltk.help.upenn_tagset('VB')

list_of_tags = []
for pair in tags:
    list_of_tags.append(pair[1])

list_of_tags = list(set(list_of_tags))
print(list_of_tags)

for pos in list_of_tags:
    print(nltk.help.upenn_tagset(pos))