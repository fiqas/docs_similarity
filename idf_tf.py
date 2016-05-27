import sys
from math import log
from collections import defaultdict
import pickle
import argparse

description = """
Script to count idf (inverted document frequency) and tf (term frequency) needed to calculate terms weights.
It may be kinda slow, 'cause it's not paralleled and it needs to check every document one by one.
So please be aware when comapring a lot, a lot of documents.
STDIN = paths to ALL documents.
"""
parser = argparse.ArgumentParser(description = description)
parser.add_argument("-d", help = "path to where dump pickles with finished calculations", required = True)
args = parser.parse_args()

def dd():
    return defaultdict(int)


if __name__ == "__main__":
    df = defaultdict(int) 
    idf = defaultdict(int)
    tf = defaultdict(dd)
    documents = [x.strip() for x in sys.stdin.readlines()]
    all_vocabulary = set()
    N = len(documents)

    print("Loaded corpora", file = sys.stderr)

    for i, document in enumerate(documents):
        print("Analyzing document", i, "/", N, file = sys.stderr)
        with open(document) as d:
            words = d.read().split()
        
        for word in words:
            tf[document][word] += 1 
        doc_voc = set(words)
        all_vocabulary.update(doc_voc)
        for word in doc_voc:
            df[word] += 1

    print("Finished counting df and tf", len(tf), len(df), file = sys.stderr)

    for word in all_vocabulary:
        idf[word] = log(N / df[word])

    print("Finished counting idf", file = sys.stderr)

    print("Finished everything, dumping...", len(all_vocabulary), file = sys.stderr)

    with open(args.d + "tf.pickle", 'wb') as pickle_f:
        pickle.dump(tf, pickle_f)

    with open(args.d + "idf.pickle", 'wb') as pickle_f:
        pickle.dump(idf_overlap, pickle_f)

