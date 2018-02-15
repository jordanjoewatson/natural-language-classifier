#!/usr/bin/python3
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


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
  if(wordCount(txt) == 0): return 0
  return(len(stringWithoutStopwords(txt))/wordCount(txt))


# pointless method but may be cleaner when writing the rest if all of the processing is done within functions from this file
def stringLength(text):
  return len(text)

def capitaliseWords(text):
  return text.title()

capitaliseWords("capitales this please?")
stringLength("what is the length of this strings?")
percentageWithoutStopwords("Get the perceptage of words without stopwords to string with them")

