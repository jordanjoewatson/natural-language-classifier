#!/usr/local/bin/python3
from sys import exit

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

def Δθ(answer,ε,θ):
  Δθp = answer - ε
  return (θ + Δθp)

def train(tData,tResult,weights,σ,θ):
  ε = σ(Σ(tData,weights) + θ)
  if(ε == tResult): return (weights,θ)
  else:
    Δweights = Δw(tData,weights,tResult,ε)
    Δbias = Δθ(tResult,ε,θ)
    return train(tData,tResult,Δweights,σ,Δbias)

def compute(data,result,weights,σ,θ):
  if((σ(Σ(data,weights) + θ)) == result): return True
  else: return False
