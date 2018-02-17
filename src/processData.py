#!/usr/local/bin/python3
from words import wordAnalysis as words
from words import syllableAnalysis as syllables
from characters import characterAnalysis as chars
from meanings import speechTags as speech
from meanings import entityAnalysis as entities


def test(s): 
  text = "The tall man ran towards the dark cold house. Hello, today I went to the shop, the shop was in the borough of Paddington in London, was that really today? I completely forgot! I thought that was yesterday, oh but maybe it was, perhaps I need to write a diary, this is some English lorem ipsum text example, just some stupid bullshit to test out my ideas! Yeah, you understand? Bonjour madame, commen't tu t'appele. Jardin Francais This is a really big house, it's huge! It was a very warm day for the beautiful human, they gracefully ran towards the cold and dark house that sat precariously on the edge of a tall cliff"
  text = "The talll man ran towards the dark cold house while the sun shon brightly on the opening to the dark lonely cave. The blind man sat calmly waiting for the time that would result in a beautifully executed something"
  text = s

  wordsLs = words.wordList(text)

  #WORD ANALYSIS
  wordCount = words.wordCount(text)
  stopwordsPercent = words.percentageWithoutStopwords(text)
  avgWordLength = words.avgWordLen(text)
  stringLength = words.stringLength(text)
  averageSyllables = syllables.averageSyllables(text)

  print(wordCount)
  print(avgWordLength)
  print(stringLength)
  print(averageSyllables)

  print(stopwordsPercent)  

  #CHARACTER ANALYSIS
  charDict = chars.updateDict(text)
  firstCharDict = chars.updateFirstChar(wordsLs)
  consecutiveCharDict = chars.updateConsecutiveChar(text)

  print(charDict)
  print(firstCharDict)
  print(consecutiveCharDict)

  #METASEMANTICS ANALYSIS
  alphaPercent = entities.alphaPercentage(text,wordCount)
  entityPercent = entities.entityPercentage(text,wordCount)

  print(alphaPercent)
  print(entityPercent)  

  speech.updateTags(text)
  nounPercent = speech.nounPercentage(wordCount)
  verbPercent = speech.verbPercentage(wordCount)
  adjPercent = speech.adjPercentage(wordCount)
  pronounPercent = speech.pronounPercentage(wordCount)
  conjunctionPercent = speech.conjunctionPercentage(wordCount)
  digitPercent = speech.digitPercentage(wordCount)
  foreignPercent = speech.foreignPercentage(wordCount)
  listPercent = speech.listPercentage(wordCount)
  toPercent = speech.toPercentage(wordCount)
  interjectionPercent = speech.interjectionPercentage(wordCount)
  possessivePercent = speech.possessivePercentage(wordCount)
  adverbPercent = speech.adverbPercentage(wordCount)
  determinerPercent = speech.determinerPercentage(wordCount)
  anonPercent = speech.anonPercentage(wordCount)
  print((verbPercent))
  print((nounPercent))
  print((adjPercent))
  print((pronounPercent))
  print((conjunctionPercent))
  print((digitPercent))
  print((foreignPercent))
  print((listPercent))
  print((toPercent))
  print((interjectionPercent))
  print((determinerPercent))
  print((possessivePercent))
  print((adverbPercent))
  print((anonPercent)) 

  nounList = speech.getNounList()
  verbList = speech.getVerbList()  
  adjList = speech.getAdjectiveList()
  pronounList = speech.getPronounList()
  conjunctionList = speech.getConjunctionList()
  digitList = speech.getDigitList()
  adverbList = speech.getAdverbList()
  foreignList = speech.getForeignList()
  listList = speech.getListList()
  toList = speech.getToList()
  interjectionList = speech.getInterjectionList()
  determinerList = speech.getDeterminerList()
  posList = speech.getPossessiveList()
  anonList = speech.getAnonList()
  
  print(adjList)
  print(pronounList)
  print(nounList)
  print(verbList)
  print(conjunctionList)
  print(digitList)
  print(adverbList)
  print(foreignList)
  print(listList)
  print(toList)
  print(interjectionList)
  print(determinerList)
  print(posList)
  print(anonList)

test("test sentence")
