import matplotlib.pyplot as plt
text = """Welcome to cognitive science lab. Todays lab class would be about NLP. On this experiment we do tokenization experiment."""

from nltk.tokenize import word_tokenize
word_tokenized = word_tokenize(text)
print(word_tokenized)

from nltk.tokenize import sent_tokenize
sentence_tokenized = sent_tokenize(text)
print(sentence_tokenized)

from nltk.probability import FreqDist
Frequent_Distribution = FreqDist(word_tokenized)
print(Frequent_Distribution.most_common(3))
Frequent_Distribution.plot(30,cumulative=False)
plt.show()