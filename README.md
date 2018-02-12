# language-expressions

Experimenting with Neural Networks in python using NLP and supervised learning to try and classify strings of text using previous examples where there doesn't seem to be any obvious pattern to identify those that should be approved. A quasi regex that doesn't have a strict pattern to work from.

A use may be to classify strings written by a certain user apart from those written by others

Another use may be to try and identify a scam email based on it's body or email subject.

The input layers for the Neural Network will be split into three specific areas that eventually come together. These are characters, words, and meanings

## Requirements

python3

nltk

spacy

## Neural Network Design

### Characters

The characters input node/s are concerned with the amount of each character that is used.

### Words

The words input node/s are concerned with things like the length of a string, types of words, more meta-data kind of analysis

### Meanings

The meanings input node/s are concerned with trying to derive subtle meanings from the words with again meta-data analysis

