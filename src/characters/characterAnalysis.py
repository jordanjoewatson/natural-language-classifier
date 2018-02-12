#!/usr/bin/python3
import re

ls = []

#Create a list of all ascii characters to use
for i in range(33,127):
  ls.append(chr(i))

#Create dictionary with all ascii characters with their value at 0
alphabet = {key: 0 for key in ls} 

#analyse the string provided, for each character incrmeent the value in the dictionary
def updateDict(str):
  if(len(str) > 0): 
    alphabet[str[0:1]] += 1
    updateDict(str[1:])

