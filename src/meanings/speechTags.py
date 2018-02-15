#!/usr/bin/python3
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer

WORD_LENGTH = 100

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


def populateLists(speechTags):
  i = 0
  for tag in speechTags:
    if(tag in nounTags): nounList[i] = 1
    elif(tag in adjectiveTags): adjectiveList[i] = 1
    elif(tag in adverbTags): adverbList[i] = 1
    elif(tag in pronounTags): pronounList[i] = 1
    elif(tag in verbTags): verbList[i] = 1
    elif(tag in conjunctionTags): conjunctionList[i] = 1
    elif(tag in determinerTags): determinerList[i] = 1
    elif(tag in digitTags): digitList[i] = 1
    elif(tag in foreignTags): foreignList[i] = 1
    elif(tag in listTags): listList[i] = 1
    elif(tag in possessiveTags): possessiveList[i] = 1
    elif(tag in toTags): toList[i] = 1
    elif(tag in interjectionTags): interjectionList[i] = 1
    else: anonList[i] = 1
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


dictTags = speechTagDict("This is a test")

textTagLs = getTagList(speechTagging("THIS IS a test example haha how are you?"))
populateLists(textTagLs)
printLists()
