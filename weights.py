
from collections import Counter
from collections import defaultdict
from math import log, sqrt, pow
import pickle
import sys
import argparse

description = """
Script to word weights for all documents.
It may be kinda slow, 'cause it's not paralleled and it needs to check every document one by one.
So please be aware when comapring a lot, a lot of documents.
"""

parser = argparse.ArgumentParser(description = description)
parser.add_argument("-d", help = "path to where are pickles with idf and tf and where to dump pickle with calculated weights.")
args = parser.parse_args()

def dd():
    return defaultdict(int)

with open(args.d + "idf.pickle", 'rb') as pickle_f:
    idf = pickle.load(pickle_f)

with open(args.d + "tf.pickle", 'rb') as pickle_f:
    tf = pickle.load(pickle_f)

weights = defaultdict(dd)

N = len(tf.keys())
for i, document in enumerate(tf.keys()):
    print(i, "/", N)
    nom = 0
    for word in tf[document]:
        nom += pow(tf[document][word], 2) * pow(idf[word], 2)
        weights[document][word] = tf[document][word] * idf[word]

    for word in tf[document]:
        weights[document][word] = weights[document][word] / sqrt(nom)

with open(args.d + "weights.pickle", 'wb') as pickle_f:
    pickle.dump(weights, pickle_f)
