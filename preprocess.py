import sys
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import argparse

description = """
Script to preprocess documents for similarity check.
To speed up preprocessing, run script with GNU parallel.
Preprocessing includes:
    a) word tokenizing (word_tokenize - NLTK)
    b) stemming (SnowballStemmer - NLTK)
    c) filtering stopwords (stop words - NLTK)
    d) filtering by keywords (IN PROGRESS)

STDIN = paths to documents.
"""
parser = argparse.ArgumentParser(description = description)
parser.parse_args()

stops = set(stopwords.words('english'))
files = [x.strip() for x in sys.stdin.readlines()]
stemmer = SnowballStemmer("english")

for filename in files:
    print(filename)
    with open(filename) as f:
        data = f.readlines()
    with open(filename.strip(".txt") + "_filtered.txt", 'w') as f:
	    for line in data:
	        tokenized = [x for x in nltk.word_tokenize(line.strip()) if x.isalpha()]
	        stemmed = [stemmer.stem(x) for x in tokenized]
	        filtered = [x for x in stemmed if x not in stops]
                f.write(" ".join(filtered) + "\n")
