#!/usr/local/bin/python
import spacy
from sys import path
path.insert(0, '../words/wordAnalysis')
import wordAnalysis

entityLs = ["ORG","PERSON","DATE","TIME","MONEY","PERCENT","FAC","GPE","NORP","WORK_OF_ART","QUANTITY","LOC","PRODUCT","EVENT","LAW","LANGUAGE","ORDINAL","CARDINAL"]
entityDict = {entity: 0 for entity in entityLs}

nlp = spacy.load('en')

#print(doc1.similarity(doc2))

alphaLs = []

def updateAlphaLs(text):
  doc = nlp(text)
  for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_,token.is_alpha,token.is_stop)
    if(token.is_alpha): alphaLs.append(token)

def updateEntityLs(text):
  doc = nlp(text)
  for entity in doc.ents:
    print(entity.label_)
    entityDict[entity.label_] += 1

def alphaPercentage(text):
  return 0  

updateAlphaLs("I'm testing out the alpha quality in the asasdas things I'm doing 142356tafdssdf")
updateEntityLs("My friend Sherlock Holmes and John Watson, also Chuck Norris and Bruce Lee, what about Batman! I am English, my nationality is also French. I really like the highway, the Highway is great the one on the way to LAX and Heathrow Airport are really fantastic. Google and Apple are brilliant companies apart from their phones. I really like Scandinavia and Japan, also Toronto seems really cool. Trolltunga is a cool mountain, just like the Alps, I don't really no mountain names, what about K2 or K4? k2 k4 I don't know... Motorbikes are kind of cool, also pizza, Pizza from Italy would be nice to try. Also Ford cars are kind of cool. What about Hurricane Catrina, Katrina? Who cares... Or the first world War or the Holocaust. I really like Beethoven and the song All You Need Is Love. Troublemaker, trying to think of famous pieces now, the Mona Lisa, Fur Elise. Law something about law... The Equality Act of 1990 I think who gives a fuck. Norwegian is an awesome language, just like Kanji is awesome too. What about Norge? does that work? The 19th Century was cool, or the Baroque Period. I really like watching minutes go by, 1 minute, two minute, three seconds four. 100 Percent of nothing is 100% of nothing. I like money but i'm broke Even $5 is a lot to me, or £5 as well 4 pounds is cool. First I like to go to the shop then 2nd I like the sky whatever this is bullshit. 1 2 3 4 100 i liek i to pplay with names. II VII")
print(entityDict)
print(alphaLs)
