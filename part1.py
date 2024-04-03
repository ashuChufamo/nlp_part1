from textblob import TextBlob
from newspaper import Article
# import nltk

# nltk.download('punkt')

# url = 'https://en.wikipedia.org/wiki/Mathematics'  # neutral content
# url = 'https://happyact.ca/2014/04/13/the-power-of-positive-words/' # positive content
url = 'https://statmodeling.stat.columbia.edu/2021/10/25/writing-negative-blog-posts/' #negative content

article = Article(url)

article.download()
article.parse()
article.nlp()

# text = article.text
text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity #-1 to 1
print(sentiment)
