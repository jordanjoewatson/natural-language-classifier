#!/usr/local/bin/python
import spacy

nlp = spacy.load('en')

entityLs = ["ORG","PERSON","DATE","TIME","MONEY","PERCENT","FAC","GPE","NORP","WORK_OF_ART","QUANTITY","LOC","PRODUCT","EVENT","LAW","LANGUAGE","ORDINAL","CARDINAL"]


def updateAlphaLs(text):
  alphaLs = []
  doc = nlp(text)
  for token in doc:
    if(token.is_alpha): alphaLs.append(token)
  return alphaLs

def updateEntityLs(text):
  entityDict = {entity: 0 for entity in entityLs}
  doc = nlp(text)
  for entity in doc.ents:
    entityDict[entity.label_] += 1
  return entityDict

def alphaPercentage(text,wordCount):
  alphaLs = updateAlphaLs(text)
  return(len(alphaLs)/wordCount)

def entityPercentage(text,wordCount):
  entityDict = updateEntityLs(text)
  entitySum = 0
  for k,v in entityDict.items(): entitySum += v   
  return(entitySum/wordCount)
