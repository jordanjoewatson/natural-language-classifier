#!/usr/local/bin/python3
from processData import convertText as convert
from perceptron import train
from perceptron import compute
from network.activation import sign
from termcolor import cprint
from pyfiglet import figlet_format
from sys import exit, stdout
from parseData import text_to_data
from random import shuffle
import random



def run_tests(test_data,test_res,weights,bias):
  test_count = len(test_data)
  init_success = 0
  for test in range(0,test_count):
    if(compute(test_data[test],test_res[test],weights,sign,bias)):
      print("[+] Test: " + str(test) + " passed")
      init_success += 1
    else:
      print("[!] Error: Test: " + str(test) + " did not pass")

  print("[*] Success Rate: " + str(init_success/test_count) + "%")
  return init_success/test_count


def run(weights,bias,training_list,training_results,test_data,test_res):
  training_range = len(training_list) - 1
  for itr in range(0,training_range):
    inputs = training_list[itr]
    weights, bias = train(training_list[itr],training_results[itr],weights,sign,bias)

  return (weights,bias)



def analyse(bias,weights,train_data,train_res,test_data,test_res,epoch,print_at_epoch,threshold):
  init_success_rate = run_tests(test_data,test_res,weights,bias)

  epoch_print = False
  if(print_at_epoch != None): epoch_print = True

  weight_averages = []
  bias_averages = []

  print("[*] Running tests " + str(epoch) + " times")
  for i in range(0,epoch):
    if(print_at_epoch == 0):
      print("[*] Iteration: " + str(i))
      stdout.write("\033[F")
    elif(i % print_at_epoch == 0):
      if(epoch_print and (i % print_at_epoch) == 0):
        print("")
        print("")
        print("[*] Running tests:")
        success_rate = run_tests(test_data,test_res,weights,bias)
        if(success_rate >= threshold):
          weight_averages.append(weights)
          bias_averages.append(bias)

      print("[*] Iteration: " + str(i))
      stdout.write("\033[F")
    (weights,bias) = run(weights,bias,train_data,train_res,test_data,test_res) #altered here
    randomize = list(zip(train_data,train_res))
    shuffle(randomize)
    train_data, train_res = zip(*randomize)


  print("[*] Finished testing")

  weight_length = len(train_data[0])
  new_weights = [0] * weight_length
  for i in range(0,weight_length-1):
    new_weights[i] = random.uniform(-1,1)

  for weights in weight_averages:
    for itr in range(0,len(weights)):
      new_weights[itr] += weights[itr]

  successful_tests = len(weight_averages)
  success_rate = None

  if(successful_tests > 0 and epoch_print == False):
    weights = [(w/successful_tests) for w in new_weights]
    bias = (sum(bias_averages))/(len(bias_averages))
    #tests = len(test_data)
  #else:

  success_rate = run_tests(test_data,test_res,weights,bias)

  print("[*] Success rate: " + str(success_rate) + "%")
  print("[*] Change of success after training: " + str((success_rate/init_success_rate)) + "%")
