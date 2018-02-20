#!/usr/local/bin/python3
from sys import exit
from network.activation import sigmoid, tanh, sign

def Σ(xs,ws):
  ls = []
  for x,w in zip(xs,ws):
    ls.append(x*w)
  return sum(ls)

def Δw(xs,ws,answer,ε):
  λ = lambda z: ((answer - ε) * z)
  mapLs = list(map(λ,xs))
  weights = []
  for map_item,weight in zip(mapLs,ws):
    weights.append(map_item+weight)
  return weights
 

def tr(tDataLs,tResultLs,weights,σ):
  #could add check before train to check size of all lists
  print("weights: "+ str(weights))
  tData = None
  tResult = None

  if(not tDataLs or not tResultLs): exit()
  if(isinstance(tResultLs,list)): tResult = tResultLs[0]
  else: tResult = tResultLs
  if(isinstance(tDataLs[0],list)): tData = tDataLs[0]
  else: tData = tDataLs

  ε = σ(Σ(tData,weights))
  if(ε == tResult): 
    train(tDataLs[1:],tResultLs[1:],weights,σ)
  else:
    Δweights = Δw(tData,weights,tResult,ε)
    train(tDataLs,tResultLs,Δweights,σ)

def train(tData,tResult,weights,σ):
  ε = σ(Σ(tData,weights))
  if(ε == tResult): return weights
  else:
    Δweights = Δw(tData,weights,tResult,ε)
    return tr(tData,tResult,Δweights,σ)

