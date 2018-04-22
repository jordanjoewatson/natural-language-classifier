from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentiment_analyzer = SentimentIntensityAnalyzer()

def normalize(value):
  return ((value + 1) / 2)

def sentiment_analysis(text):
  ls = []
  analysis = TextBlob(text)
  ls.append(normalize(analysis.polarity))
  ls.append(analysis.subjectivity)
  ls.append(sentiment_analyzer.polarity_scores(text))
  return ls
