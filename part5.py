import nltk
# nltk.download('wordnet')
# nltk.download('vader_lexicon')

from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer


text = """Welcome to cognitive science lab. Todays lab class would be about NLP. On this experiment we do tokenization experiment."""
demoWords = ["playing","happiness","going", "go","doing", "do","yes","no","I", "Me","having","had", "coding", "programming", "code", "program"]

# lemmatizer = WordNetLemmatizer()
# stemmer = PorterStemmer()

# for word in demoWords:
#     # word stem lemmatize
#     print(word, stemmer.stem(word),lemmatizer.lemmatize(word,"v"))


sia = SentimentIntensityAnalyzer()
print(sia.polarity_scores('Programming is fun'))
print(sia.polarity_scores('I always bike to school'))
print(sia.polarity_scores('You behaved very badly today'))
print(sia.polarity_scores('You behaved very BADLY today'))
print(sia.polarity_scores('You behaved very BADLY today!!!'))
