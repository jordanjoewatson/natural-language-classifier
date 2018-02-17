#!/usr/bin/python3
import re

# May also need to add newlines \x0A into my code?
ls = []

#Create a list of all ascii characters to use
for i in range(32,127):
  ls.append(chr(i))

#analyse the string provided, for each character incrmeent the value in the dictionary
def updateDict(text):
  alphabet = {key: 0 for key in ls}
  for char in text: alphabet[char] += 1
  return [v for v in alphabet.values()]

def updateFirstChar(wordLs):
  firstCharAlphabet = {key: 0 for key in ls}
  for word in wordLs: firstCharAlphabet[word[:1]] += 1    
  return [v for v in firstCharAlphabet.values()]

# updates a dictionary with how many characters are next
# for example, i = 0, ii = 2, one cannot exist because 
def updateConsecutiveChar(text):
  consecutiveCharAlphabet = {key: 0 for key in ls}
  if(len(text) > 0):
    regexStr = r'' + re.escape(text) + ''
    consecutiveChars = re.findall(r'((.)\2{1,})',regexStr)
    for char in consecutiveChars:
      consecutiveCharAlphabet[char[1]] += len(char[0])
  return [v for v in consecutiveCharAlphabet.values()]
