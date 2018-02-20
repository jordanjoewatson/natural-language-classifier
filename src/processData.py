#!/usr/local/bin/python3
from words import wordAnalysis as words
from words import syllableAnalysis as syllables
from characters import characterAnalysis as chars
from meanings import speechTags as speech
from meanings import entityAnalysis as entities


def test(s): 

  ls = []

  text = "The tall man ran towards the dark cold house. Hello, today I went to the shop, the shop was in the borough of Paddington in London, was that really today? I completely forgot! I thought that was yesterday, oh but maybe it was, perhaps I need to write a diary, this is some English lorem ipsum text example, just some stupid bullshit to test out my ideas! Yeah, you understand? Bonjour madame, commen't tu t'appele. Jardin Francais This is a really big house, it's huge! It was a very warm day for the beautiful human, they gracefully ran towards the cold and dark house that sat precariously on the edge of a tall cliff"
  text = "The talll man ran towards the dark cold house while the sun shon brightly on the opening to the dark lonely cave. The blind man sat calmly waiting for the time that would result in a beautifully executed something"
  #text = s

  wordsLs = words.wordList(text)

  #WORD ANALYSIS
  wordCount = words.wordCount(text)
  stopwordsPercent = words.percentageWithoutStopwords(text)
  avgWordLength = words.avgWordLen(text)
  stringLength = words.stringLength(text)
  averageSyllables = syllables.averageSyllables(text)

  ls.append(wordCount)
  ls.append(stopwordsPercent)
  ls.append(avgWordLength)
  ls.append(stringLength)
  ls.append(averageSyllables)

  #CHARACTER ANALYSIS
  charDict = chars.updateDict(text)
  firstCharDict = chars.updateFirstChar(wordsLs)
  consecutiveCharDict = chars.updateConsecutiveChar(text)

  ls += charDict + firstCharDict + consecutiveCharDict

  #METASEMANTICS ANALYSIS
  alphaPercent = entities.alphaPercentage(text,wordCount)
  entityPercent = entities.entityPercentage(text,wordCount)

  ls.append(alphaPercent)
  ls.append(entityPercent)

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
  ls.append(verbPercent)
  ls.append(nounPercent)
  ls.append(adjPercent)
  ls.append(pronounPercent)
  ls.append(conjunctionPercent)
  ls.append(digitPercent)
  ls.append(foreignPercent)
  ls.append(listPercent)
  ls.append(toPercent)
  ls.append(interjectionPercent)
  ls.append(determinerPercent)
  ls.append(possessivePercent)
  ls.append(adverbPercent)
  ls.append(anonPercent)

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
 
  ls += (adjList + pronounList + nounList + verbList + conjunctionList + digitList)
  ls += (adverbList + foreignList + listList + toList + interjectionList + determinerList)
  ls += (posList + anonList) 
  #print(len(ls))
  #print(ls)

test("test sentence")
