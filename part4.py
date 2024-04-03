import nltk
# nltk.download('stopwords')

text = """Welcome to cognitive science lab. Todays lab class would be about NLP. On this experiment we do tokenization experiment."""
demoWords = ["playing","happiness","going","doing","yes","no","I","having","had"]

from nltk.corpus import stopwords
stop_words = stopwords.words('english')
# print(stop_words)

from nltk.tokenize import word_tokenize, sent_tokenize
tokenize_words = word_tokenize(text)
# print(tokenize_words)

tokenize_words_without_stop_words = []
for word in tokenize_words:
    if word not in stop_words:
        tokenize_words_without_stop_words.append(word)
        
print('Tokenized words which include the stop words',tokenize_words)
print('Tokenized words without the stop words',tokenize_words_without_stop_words)
print('Stop words which was removed',set(tokenize_words)-set(tokenize_words_without_stop_words))

