#!/usr/local/bin/python3
from processData import convertText as convert
from sys import exit

def text_to_data(filename):
  file = None
  try:
    file = open(filename,'r')
  except:
    print("[!] Error opening file: " + filename)
    exit()

  print("[*] Converting lines from file: " + filename) 

  lines = [line.rstrip('\n') for line in file]
  lines = [line for line in lines if (len(line) >= 1)]
  train_list = []
  test_list = []

  #need to take command line option to take file as input
  #need to output to a file

  for itr in range(0,int(len(lines)),2):
    data = lines[itr]
    text = lines[itr+1]
    training = False
    number = data[1:len(data)]
    if(data[len(data)-1] == 'T'): 
      training = True
      number = data[1:len(data)-1]
    else: 
      training = False
      number = data[1:len(data)]

    inputs = convert(text)
    if(training): train_list.append(inputs)
    else: test_list.append(inputs)

  file.close()
  return [train_list,test_list]

