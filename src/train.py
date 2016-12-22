
"""
Train the models.
"""

#. this will be done in the experiment notebooks


from __future__ import print_function, division
import random
from pprint import pprint

# this assumes we're running the test from the root folder with 'make test'
import sys; sys.path.append('src')
import ngram


infile = 'data/split/all-train.txt'
modelfile = 'data/models/ngram-model-basic.pickle'

n = 3

print("read file: " + infile)
f = open(infile, 'rb')
s = f.read()
s = s.strip()
s = s.lower()
f.close()

print("train model")
model = ngram.NgramModel(n)
model.train(s)

print("save model: " + modelfile)
model.save(modelfile)



