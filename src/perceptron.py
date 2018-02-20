#!/usr/local/bin/python3
from sys import exit
from network.activation import sigmoid, tanh, sign
#sum()
#

#Removes first element from list and returns it
def deque(l):
  return

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
 

def train(tDataLs,tResultLs,weights,σ):
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


train([[40,45],[20,105],[-24,63],[302,-4],[-24,-59]],[1,1,1,-1,-1],[1,1],sign)
train([[40,45],[20,105],[-24,63],[302,-4],[-24,-59]],[1,1,1,-1,-1],[1,2],sign)
