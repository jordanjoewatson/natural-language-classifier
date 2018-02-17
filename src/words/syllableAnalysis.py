#!/usr/local/bin/python3
import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict
from sys import path

dict = cmudict.dict()

def syllables(word):
  try:
    return [len(list(y for y in x if isdigit(y[-1]))) for x in dict[word.lower()]][0]
  except:
    wordLength = len(word)
    if(wordLength >= 0 and wordLength < 6): return 1
    elif(wordLength >= 6 and wordLength < 8): return 2
    elif(wordLength >= 8 and wordLength < 10): return 3
    else: return 4
  

#pass in text as a list
def averageSyllables(text):
  wordCount = len(text)
  syllableCount = 0
  for word in text: syllableCount += syllables(word)
  return syllableCount/wordCount

