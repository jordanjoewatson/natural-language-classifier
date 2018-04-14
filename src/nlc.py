import argparse
from analyse_data import analyse
from parseData import text_to_data
from random import shuffle, uniform

parser = argparse.ArgumentParser()

parser.add_argument("-e", "--epoch", help="set amount of iterations of running the training data", type=int, required=True)
parser.add_argument("-p", "--print-at-epoch", help="run the tests and print output at every nth epoch", type=int)
parser.add_argument("-t", "--threshold", help="specify threshold for successful test percentage, at every epoch print specified, if success is over the threshold value then store the current weights in an array, at the end of the training period, find the average of all succesful weights", type=float)
parser.add_argument("-b", "--bias", default=0, help="set starting bias, if empty then defaults to 0", type=int)
parser.add_argument("-it", "--input-text", default=[], nargs='*', help="specify text files to use", type=str)
parser.add_argument("-id", "--input-data", default=[], nargs='*', help="specify converted text files to use", type=str)
parser.add_argument("-r", "--read-weights", help="specify file containing previously used weights", type=str)
parser.add_argument("-w", "--write-weights", help="write weights to file at the print at epoch and final weights", type=str)
parser.add_argument("-c", "--convert", help="convert text file to data for quick use", type=str)

args = parser.parse_args()

#COULD also randomise data for every batch used to train

epoch = args.epoch
bias = args.bias

print_at_epoch = None
if(args.print_at_epoch == None):
  print_at_epoch = 0
else:
  print_at_epoch = args.print_at_epoch

average_weights = False
threshold = None
if(args.threshold != None):
  threshold = args.threshold
  average_weights = True

txt_file_one = None
txt_file_two = None
data_file_one = None
data_file_two = None

#input text == 2 || input data == 2
if(args.input_data == [] and len(args.input_text) == 2):
  txt_file_one = args.input_text[0]
  txt_file_two = args.input_text[1]
elif(args.input_text == [] and len(args.input_data) == 2):
  data_file_one = args.input_data[0]
  data_file_two = args.input_data[1]
else:
  print("[!] Need to specify input data")
  print("      python3 nlc.py -it text_file_one.txt text_file_two.txt")
  print("      python3 nlc.py -id data_file_one.txt data_file_two.txt")

#Add functionality for converting text to data only
#write weights to file
#read weights from file



file_one_list = text_to_data("examples/meditations.txt") #two.txt
file_two_list = text_to_data("examples/leviathan.txt") #on_libert.txt

file_one_training = file_one_list[0]
file_two_training = file_two_list[0]

#tests don't need to be randomize as they don't train
file_one_test = file_one_list[1]
file_two_test = file_two_list[1]

file_one_train_results = [1] * len(file_one_training)
file_one_test_results = [1] * len(file_one_test)

file_two_train_results = [-1] * len(file_two_training)
file_two_test_results = [-1] * len(file_two_test)

training_list = file_one_training + file_two_training
training_results = file_one_train_results + file_two_train_results

test_list = file_one_test + file_two_test
test_results = file_one_test_results + file_two_test_results

#Randomize order of results
randomize = list(zip(training_list,training_results))
shuffle(randomize)
training_list,training_results = zip(*randomize)

#create list of correct length for weights
l = len(training_list[0])
weights = [0] * l
for i in range(0,l-1):
  weights[i] = uniform(-1,1)

analyse(bias,weights,training_list,training_results,test_list,test_results,epoch,print_at_epoch,threshold)
