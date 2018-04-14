#!/usr/bin/python3
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer

WORD_LENGTH = 250

nounSum = 0
adjectiveSum = 0
pronounSum = 0
adverbSum = 0
verbSum = 0
conjunctionSum = 0
determinerSum = 0
digitSum = 0
foreignSum = 0
listSum = 0
posSum = 0
toSum = 0
interjectionSum = 0
anonSum = 0

# These should now hopefully be correct
nounTags = ["NN","NNS","NNP","NNPS"]
adjectiveTags = ["JJ","JJR","JJS"]
pronounTags = ["PRP","PRP$","WP","WP$"]
adverbTags = ["RB","RBS","RBR","WRB"]
verbTags = ["VB","VBD","VBG","VBN","VBP","VBZ"]
conjunctionTags = ["CC","IN"]
determinerTags = ["DT","WDT"]
digitTags = ["CD"]
foreignTags = ["FW"]
listTags = ["LS"]
possessiveTags = ["POS"]
toTags = ["TO"]
interjectionTags = ["UH"]
anonTags = [] #Don't need to define as else statement

nounList = [0] * WORD_LENGTH
adjectiveList = [0] * WORD_LENGTH
adverbList = [0] * WORD_LENGTH
pronounList = [0] * WORD_LENGTH
verbList = [0] * WORD_LENGTH
conjunctionList = [0] * WORD_LENGTH
determinerList = [0] * WORD_LENGTH
digitList = [0] * WORD_LENGTH
foreignList = [0] * WORD_LENGTH
listList = [0] * WORD_LENGTH
possessiveList = [0] * WORD_LENGTH
toList = [0] * WORD_LENGTH
interjectionList = [0] * WORD_LENGTH
anonList = [0] * WORD_LENGTH

#Finish for debugging?
def printSums():
  print(nounSum)
  print(adjectiveSum)
  print(adverbSum)

def printLists():
  print(nounList)
  print(adjectiveList)
  print(adverbList)
  print(pronounList)
  print(verbList)
  print(conjunctionList)
  print(determinerList)
  print(digitList)
  print(foreignList)
  print(listList)
  print(possessiveList)
  print(toList)
  print(interjectionList)
  print(anonList)

def resetSums():
  global nounSum, adjectiveSum, adverbSum, pronounSum, verbSum, conjunctionSum, determinerSum
  global anonSum, digitSum, foreignSum, listSum, posSum, toSum, interjectionSum
  nounSum = 0
  adjectiveSum = 0
  adverbSum = 0
  pronounSum = 0
  verbSum = 0
  conjunctionSum = 0
  determinerSum = 0
  digitSum = 0
  foreignSum = 0
  listSum = 0
  posSum = 0
  toSum = 0
  interjectionSum = 0
  anonSum = 0

def resetLists():
  global nounList, adjectiveList, adverbList, pronounList, verbList, conjunctionList
  global determinerList, digitList, foreignList, listList, possessiveList, toList
  global interjectionList, anonList
  nounList = [0] * WORD_LENGTH
  adjectiveList = [0] * WORD_LENGTH
  adverbList = [0] * WORD_LENGTH
  pronounList = [0] * WORD_LENGTH
  verbList = [0] * WORD_LENGTH
  conjunctionList = [0] * WORD_LENGTH
  determinerList = [0] * WORD_LENGTH
  digitList = [0] * WORD_LENGTH
  foreignList = [0] * WORD_LENGTH
  listList = [0] * WORD_LENGTH
  possessiveList = [0] * WORD_LENGTH
  toList = [0] * WORD_LENGTH
  interjectionList = [0] * WORD_LENGTH
  anonList = [0] * WORD_LENGTH

def populateLists(speechTags):
  global nounSum, adjectiveSum, adverbSum, pronounSum, verbSum, conjunctionSum, determinerSum
  global anonSum, digitSum, foreignSum, listSum, posSum, toSum, interjectionSum
  i = 0
  for tag in speechTags:
    if(tag in nounTags): 
      nounList[i] = 1
      nounSum += 1
    elif(tag in adjectiveTags): 
      adjectiveList[i] = 1
      adjectiveSum += 1
    elif(tag in adverbTags): 
      adverbList[i] = 1
      adverbSum += 1
    elif(tag in pronounTags): 
      pronounList[i] = 1
      pronounSum += 1
    elif(tag in verbTags): 
      verbList[i] = 1
      verbSum += 1
    elif(tag in conjunctionTags): 
      conjunctionList[i] = 1
      conjunctionSum += 1
    elif(tag in determinerTags): 
      determinerList[i] = 1
      determinerSum += 1
    elif(tag in digitTags): 
      digitList[i] = 1
      digitSum += 1
    elif(tag in foreignTags): 
      foreignList[i] = 1
      foreignSum += 1
    elif(tag in listTags):
      listList[i] = 1
      listSum += 1
    elif(tag in possessiveTags):
      possessiveList[i] = 1
      posSum += 1
    elif(tag in toTags): 
      toList[i] = 1
      toSum += 1
    elif(tag in interjectionTags):
      interjectionList[i] = 1
      interjectionSum += 1
    else: 
      anonList[i] = 1
      anonSum += 1
    i += 1 


tagList = ["CC","CD","DT","EX","FW","IN","JJ","JJR","JJS","LS","MD","NN","NNS","NNP",
           "PDT","POS","PRP","PRP$","RB","RBR","RBS","RP","TO","UH","VB","VBD","VBG",
           "VBN","VBP","VBZ","WDT","WP","WP$","WRB"]

# get a list of tags from a list of tuples of words and tags
# INPUT: list of tuple [("Word","DT"),("WORD2","NN")]
# OUTPUT: list of tag types ["DT","NN"]
# to be used to get list of speech tags in the order they are in the sentence
def getTagList(tuples):
  ls = []
  for tuple in tuples:
    ls.append(tuple[1])
  return ls

#creates a tuple list of words and their tags from the text
#converts "This is a sentence" to ("This","DT"),...
def speechTagging(text):
  tags = []
  custom_tokenizer = PunktSentenceTokenizer(text)
  tokenized = custom_tokenizer.tokenize(text)
  try:
    for i in tokenized:
      words = nltk.word_tokenize(i)
      tagged = nltk.pos_tag(words)
      tags += tagged 
  except Exception as e:
    print(str(e))
  return tags

#creates a dictionary of recurrance of speech tags in text
def speechTagDict(text):
  dict = {key: 0 for key in tagList}
  tupleTags = speechTagging(text)
  for tuple in tupleTags:
    dict[tuple[1]] += 1
  return dict

def nounPercentage(wordCount):
  return(nounSum/wordCount)

def verbPercentage(wordCount):
  return(verbSum/wordCount)  

def adjPercentage(wordCount):
  return(adjectiveSum/wordCount)

def adverbPercentage(wordCount):
  return(adverbSum/wordCount)

def pronounPercentage(wordCount):
  return(pronounSum/wordCount)

def conjunctionPercentage(wordCount):
  return(conjunctionSum/wordCount)

def digitPercentage(wordCount):
  return(digitSum/wordCount)

def possessivePercentage(wordCount):
  return(posSum/wordCount)

def foreignPercentage(wordCount):
  return(foreignSum/wordCount)

def listPercentage(wordCount):
  return(listSum/wordCount)

def toPercentage(wordCount):
  return(toSum/wordCount)

def determinerPercentage(wordCount):
  return(determinerSum/wordCount)

def interjectionPercentage(wordCount):
  return(interjectionSum/wordCount)

def anonPercentage(wordCount):
  return(anonSum/wordCount)

def getNounList():
  return nounList

def getDeterminerList():
  return determinerList

def getPossessiveList():
  return possessiveList

def getAdjectiveList():
  return adjectiveList

def getAdverbList():
  return adverbList

def getVerbList():
  return verbList

def getPronounList():
  return pronounList

def getConjunctionList():
  return conjunctionList

def getDigitList():
  return digitList

def getForeignList():
  return foreignList

def getListList():
  return listList

def getToList():
  return toList

def getInterjectionList():
  return interjectionList

def getAnonList():
  return anonList

#Finish off the rest

#dictTags = speechTagDict("This is a test")

def updateTags(text):
  resetLists()
  resetSums()
  textTagLs = getTagList(speechTagging(text))
  populateLists(textTagLs)

#textTagLs = getTagList(speechTagging("THIS IS a test example haha how are you?"))
#populateLists(textTagLs)
