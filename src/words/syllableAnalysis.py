#!/usr/local/bin/python3
import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict
from sys import path
from math import exp as e

def f(x):
  fr = (1/(1+e(-x)))
  min = fr - 0.5
  return min*2

dict = cmudict.dict()

def syllables(word):
  val = 1
  try:
    val = [len(list(y for y in x if isdigit(y[-1]))) for x in dict[word.lower()]][0]
  except:
    wordLength = len(word)
    if(wordLength >= 0 and wordLength < 6): val = 1
    elif(wordLength >= 6 and wordLength < 8): val = 2
    elif(wordLength >= 8 and wordLength < 10): val = 3
    else: val = 4

  if(val == 1 or val == 0): return 0
  elif(val == 2): return 0.2
  elif(val == 3): return 0.4
  elif(val == 4): return 0.6
  elif(val == 5): return 0.8
  else: return 1
  return (val) #Maybe need to make the difference from 1 -> 10 larger
               #instead of not using it at all, so alter f, i.e normalise differentiyl
               #in this case


#pass in text as a list
def averageSyllables(text):
  wordCount = len(text)
  syllableCount = 0
  for word in text: syllableCount += syllables(word)
  return syllableCount/wordCount
