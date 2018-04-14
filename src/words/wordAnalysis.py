#!/usr/bin/python3
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from math import exp as e

MAX_WORDS = 250

def f(x):
  fr = (1/(1+e(-x)))
  min = fr - 0.5
  return 2*min

def wordList(text):
  wordLs = []
  for word in text.split(" "):
    if(len(word) > 0): wordLs.append(word)
  return wordLs

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
  return (wordCount/MAX_WORDS)

#gets average length of words in string
def avgWordLen(text):
  #get amount of words in strings
  wordLs = text.split(" ")
  word_count = len(wordLs)
  current_max_word = 0
  total_string_length = 0
  for word in wordLs:
    temp_word_length = len(word)
    total_string_length += temp_word_length
    if(temp_word_length > current_max_word): current_max_word = temp_word_length

  return (total_string_length/(current_max_word*word_count))
  #for each word in string, get the maximum length
  #string length += length of words
  #string length / max word length squared
  #wordCnt = wordCount(text)
  #if(wordCnt == 0): wordCnt = 0
  #noSpaces = re.sub(' ','',text)
  #red = f((len(noSpaces) / wordCnt)) #remove
  #return red

def percentageWithoutStopwords(txt):
  #print(len(stringWithoutStopwords(txt)))
  #print(wordCount(txt))
  if(wordCount(txt) == 0): return 0
  return((len(stringWithoutStopwords(txt))/MAX_WORDS)/wordCount(txt))


# pointless method but may be cleaner when writing the rest if all of the processing is done within functions from this file
#ALTERING THIS MAYBE CHANGE BACK
def stringLength(text):
  l = len(text)
  return l/2500  #was f(l)  afer l now <=

def capitaliseWords(text):
  return text.title()

#capitaliseWords("capitales this please?")
#stringLength("what is the length of this strings?")
#percentageWithoutStopwords("Get the perceptage of words without stopwords to string with them")
