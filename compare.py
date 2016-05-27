from collections import Counter
from collections import defaultdict
from math import log, sqrt, pow
import pickle
import sys
import argparse

description = """
Script to compare documents.
It's very fast, 'cause it only uses weight pickle.
It shows top 30 similar documents to that one chosen.
"""
parser = argparse.ArgumentParser(description = description)
parser.add_argument("-d", help = "path to where weight.pickle is", required = True)
parser.parse_args()

def dd():
    return defaultdict(int)

def calculate_scores(query, documents, weights, scores):
    query_words = set(weights[query].keys())

    for document in documents:
        score = 0
        nom = 0
        for word in query_words:
            score += weights[query][word] * weights[document][word]
        scores[document] = score

    return sorted(scores, key = scores.get, reverse = True)[:30]
            

if __name__ == "__main__":
    scores = {}

    with open(args.d + "weights.pickle", 'rb') as pickle_f:
        weights = pickle.load(pickle_f)

    print("Loaded pickles...", file = sys.stderr)
    while True:
        filename = input("Input file name to compare:\n")
        scored_docs = calculate_scores(filename, weights.keys(), weights, scores)
        print("-----------------------")
        print("TOP 30 SIMILAR DOCUMENTS")
        print("-----------------------")
        for i, document in enumerate(scored_docs):
            print(str(i + 1) + ")", document, scores[document])
        print("-----------------------")

