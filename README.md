# natural-language-classifier

Experimenting with a perceptron in python using NLP and supervised learning to try and classify strings of text using previous examples where there doesn't seem to be any obvious way to classify them.

## Requirements

python3

nltk

spacy

## Analysis

### Characters

The characters inputs are concerned with the amount of each character that is used.

### Words

The words inputs are concerned with things like the length of a string, types of words, more meta-data kind of analysis

### Meanings/Meta Semantics

The meanings inputs are concerned with trying to derive subtle meanings from the words

## Success

Has been able to classify sentences from the following texts

95% Success Rate comparing Thomas Hobbes - Leviathan && Rene Descartes - Meditations

95% Success Rate comparing John Stuart Mill - On Liberty && Shakespeare - The Tempest

77% Success Rate comparing John Stuart Mill - On Liberty && John Stuart Mill - Utilitarianism

## Usage

There are two ways of running the classifier

### 1

This way will run the classifier with an epoch of 100, and running on the input text files.

```
python3 nlc.py -it file_one.txt file_two.txt -e 100
```

### 2

This way will run the classifier with the input files as before, with an optional bias value of 7, if left blank it will default to 0.

Setting the threshold and print_at_epoch values will mean that at every 10th epoch the classifier will run the tests, print the output, and if the success rate is higher or equal to the threshold it will store the current set of weights. At the end if there are any weights saved then the weights will be averaged and the final tests will be run with those weights.

```
python3 nlc.py -it file_one.txt file_two.txt -e 1000 -t 0.8 -p 10 -b 7
```

## Preparing Data

To write files containing data to test it needs to be in the format of

```
#1T 
This is the first training example that will be tested and alter the weights with.

#2T
This is the second, every time an epoch is finished the ordering is randomized to try and maximize success

#3
After writing training examples this is how you write the tests that will be used to test the success, these will not be included in the training data to train perceptron
```

When testing against two different files the files need to have the same amount of training data

See the example directory for examples and something to use to run the classifier
