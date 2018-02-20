#!/usr/local/bin/python3
from processData import convertText as convert

ls = ["test@example.org","exampleemail@testing.org","something@yes.com"]

data = []
for text in ls:
  data.append(convert(text))

#data is now list of converted data
print(data)
