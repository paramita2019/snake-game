# write code to analyze sentiment of a text
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.classify import ClassifierI
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random

class Classifier(ClassifierI):
    def __init__(self):
        self._model = None

    def train(self):

        # Get the movie reviews
        reviews = [(list(movie_reviews.words(fileid)), category)
                   for category in movie_reviews.categories()
                   for fileid in movie_reviews.fileids(category)]

        # Shuffle the reviews
        random.shuffle(reviews)

        # Get the stop words
        stop_words = set(stopwords.words('english'))

        # Get the words in the reviews
        all_words = []
        for review in reviews:
            for word in review[0]:
                if word.lower() not in stop_words:
                    all_words.append(word.lower())

        # Get the frequency distribution of the words
        all_words = nltk.FreqDist(all_words)

        # Get the top 3000 words
        word_features = list(all_words.keys())[:3000]

        # Get the features
        featuresets = [(find_features(review, word_features), category) for (review, category) in reviews]

        # Train the model
        self._model = nltk.NaiveBayesClassifier.train(featuresets)

    def classify(self, text):
        # Get the features of the text
        features = find_features(text, list(self._model.most_informative_features())[:3000])

        # Classify the text
        return self._model.classify(features)

def find_features(document, word_features):
    words = set(document)
    features = {}
    for word in word_features:
        features[word] = (word in words)
    return features

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    print(sentiment)
    return sentiment

# write a main method to test the functions
main():
    text = input("Enter the text to analyze: ")
    sentiment = analyze_sentiment(text)
    if sentiment['compound'] >= 0.05:
        print("Positive sentiment")
    elif sentiment['compound'] <= -0.05:
        print("Negative sentiment")
    else:
        print("Neutral sentiment")

    classifier = Classifier()
    classifier.train()

    #text = input("Enter the text to classify: ")
    category = classifier.classify(word_tokenize(text))
    print(f"The category of the text is: {category}")