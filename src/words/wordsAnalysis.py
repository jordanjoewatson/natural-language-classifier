#!/usr/bin/python3
import re
import spacy
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer

tagList = ["CC","CD","DT","EX","FW","IN","JJ","JJR","JJS","LS","MD","NN","NNS","NNP",
           "PDT","POS","PRP","PRP$","RB","RBR","RBS","RP","TO","UH","VB","VBD","VBG",
           "VBN","VBP","VBZ","WDT","WP","WP$","WRB"]

def stringWithoutStopwords(text):
  stop_words = set(stopwords.words('english'))
  word_tokens = word_tokenize(text)
  filtered_sentence = [word for word in word_tokens if not word in stop_words]
  return(filtered_sentence)

#gets the amount of words in a string
def wordCount(text):
  wordLs = text.split(" ")
  wordCount = 0
  for word in wordLs:
    if(len(word) > 0): wordCount += 1
  return wordCount

#gets average length of words in string
def avgWordLen(text):
  wordCnt = wordCount(text)
  if(wordCnt == 0): return 0
  noSpaces = re.sub(' ','',text)
  return(len(noSpaces) / wordCnt) 
 
def percentageWithoutStopwords(txt):
  print(txt)
  if(wordCount(txt) == 0): return 0
  return(len(stringWithoutStopwords(txt))/wordCount(txt))

#creates a tuple list of words and their tags
def speechTagging(text):
  custom_tokenizer = PunktSentenceTokenizer(text)
  tokenized = custom_tokenizer.tokenize(text)
  try:
    for i in tokenized:
      words = nltk.word_tokenize(i)
      tagged = nltk.pos_tag(words)
      return(tagged)
  except Exception as e:
    print(str(e))

#creates a dictionary of recurrance of speech tags in text
def speechTagDict(text):
  dict = {key: 0 for key in tagList}
  tupleTags = speechTagging(text)
  for tuple in tupleTags:
    dict[tuple[1]] += 1
  return dict



#speechTagging("This is a test email@email.org at 1:00PM on Thursday with John in UK")
speechTagDict("This is a test")
