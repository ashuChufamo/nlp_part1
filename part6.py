import nltk
from nltk.corpus import wordnet

# syn = wordnet.synsets('Computer')
# print(syn)
# print(syn[0].definition())

synonyms = []
for syn in wordnet.synsets('Computer'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print(synonyms)

antonyms = []
for ant in wordnet.synsets('Small'):
    for lemma in ant.lemmas():
       if lemma.antonyms():
           antonyms.append(lemma.antonyms()[0].name())
print(antonyms)