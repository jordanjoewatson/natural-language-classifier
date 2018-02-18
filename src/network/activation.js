#!/usr/local/bin/python3
import numpy as np
from math import exp as e

LEAKY = 0.01

'''
Could add a higher learning rate for when the gradient is very low or very high
  to adjust the vanishing gradient problem
Ideally sign would be best for saying yes this is 1 => true else -1 => false
However sign doesn't have a gradient in differentiation. Therefore
Could use sigmoid or tanh and could say if y in range [0..1] => true, else
in range of [-1..0] => false

compute(trainingData,trainingResult)
if(output in range of True/[0..1]) => return
else: backpropagate(error)

tanh seems a good candidate for outputs
leaky ReLu seems good for hidden layers

softmax is good for output neuron when having multiple possiblities

ReLU only for hidden layers

Sigmoid
Sigmoid'
tanh
tanh'
sign
?sign'
'''

def softmax(x):
  ex = np.exp(x)
  sum_ex = np.sum(np.exp(x))
  return ex/sum_ex

def tanh(x):
  e_x = e(x)
  e_mx = e(-x)
  return((e_x-e_mx)/(e_x+e_mx))

def tanhPrime(x):
  e_x = e(x)
  e_mx = e(-x)
  numerator = (e_x - e_mx)**2
  denominator = (e_x + e_mx)**2
  return(1-(numerator/demoninator))

def sigmoid(z):
  return(1/(1+e(-z)))

def sigmoidPrime(x):
  return(sigmoid(x) * (1 - sigmoid(x)))

def leakyReLU(x):
  if(x > 0): return max(0,x)
  else: return LEAKY*x

def leakyReLUPrime(x):
  if(x > 0): return 1
  else: return LEAKY
