#!/usr/bin/python3
import re

# May also need to add newlines \x0A into my code?

ls = []

#Create a list of all ascii characters to use
for i in range(32,127):
  ls.append(chr(i))

#Create dictionary with all ascii characters with their value at 0
alphabet = {key: 0 for key in ls} 
firstCharAlphabet = {key: 0 for key in ls}
consecutiveCharAlphabet = {key: 0 for key in ls}

#analyse the string provided, for each character incrmeent the value in the dictionary
def updateDict(text):
  if(len(text) > 0): 
    alphabet[text[0:1]] += 1
    updateDict(text[1:])

def updateFirstChar(text):
  wordLs = []
  for word in text.split(" "):
    if(len(word) > 0): wordLs.append(word)
  for word in wordLs: firstCharAlphabet[word[:1]] += 1    

# updates a dictionary with how many characters are next
# for example, i = 0, ii = 2, one cannot exist because 
def updateConsecutiveChar(text):
  if(len(text) > 0):
    regexStr = r'' + re.escape(text) + ''
    consecutiveChars = re.findall(r'((.)\2{1,})',regexStr)
    for char in consecutiveChars:
      consecutiveCharAlphabet[char[1]] += len(char[0])
    print(consecutiveCharAlphabet)

updateFirstChar("Hey is this working?   Hahaa yeah i think ")
updateDict("Hey is this working?   haha yeah i tihnk so?")
print(firstCharAlphabet)
print(alphabet)
updateConsecutiveChar("Hey iiiiss  TThiss woRRkiNg")
print(consecutiveCharAlphabet)
