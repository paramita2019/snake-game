# write code to analyze sentiment of a text
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#   nltk.download('vader_lexicon')
#   # nltk.download('punkt')
#   # nltk.download('averaged_perceptron_tagger')
#   # nltk.download('maxent_ne_chunker')
#   # nltk.download('words')
#   # nltk.download('stopwords')
#   # nltk.download('wordnet')
#   # nltk.download('omw')
#   # nltk.download('universal_tagset')
#   # nltk.download('tagsets')
#   # nltk.download('brown')
#   # nltk.download('names')
#   # nltk.download('movie_reviews')
#   # nltk.download('treebank')
#   # nltk.download('wordnet_ic')


def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    print(sentiment)
    return sentiment

text = input("Enter the text to analyze: ")

sentiment = analyze_sentiment(text)

if sentiment['compound'] >= 0.05:
    print("Positive sentiment")

elif sentiment['compound'] <= -0.05:
    print("Negative sentiment")

else:
    print("Neutral sentiment")
s