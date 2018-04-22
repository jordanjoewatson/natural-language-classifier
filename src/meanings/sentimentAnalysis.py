from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentiment_analyzer = SentimentIntensityAnalyzer()

'''
def getPolarity(text):
  polarity = TextBlob(text).polarity
  print(polarity)
  return (((polarity + 1) * 10) / 2);


def getSubjectivity(text):
	analysis = TextBlob(inputString)
    return TextBlob(text).subjectivity
	return analysis.subjectivity*10 #normalize data to 0..10
'''

def normalize(value):
  return ((value + 1) / 2)

def sentiment_analysis(text):
  ls = []
  analysis = TextBlob(text)
  ls.append(normalize(analysis.polarity))
  ls.append(analysis.subjectivity)
  ls.append(sentiment_analyzer.polarity_scores(text))
  return ls
