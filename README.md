# language-expressions

Experimenting with Neural Networks in python to try and create something that behaves similar to a regex but without knowing the specific pattern of characters even if one may or may not exist.

A use may be to classify strings written by a certain user.
Another use may be to try and identify a scam email.
Another use that may not be entirely useful could be to try and use these language expression idea to identify something that belongs to a regex.

The input layers for the Neural Network will be split into three specific areas that eventually come together. These are characters, words, and meanings

## Requirements

python3
nltk
spacy

### Characters

The characters input node/s are concerned with the amount of each character that is used.

### Words

The words input node/s are concerned with things like the length of a string, types of words, more meta-data kind of analysis

### Meanings

The meanings input node/s are concerned with trying to derive subtle meanings from the words with again meta-data analysis

