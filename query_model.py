import csv
import os
import string
import multiprocessing
import codecs
import nltk                             # pip3 install nltk
import sklearn.manifold                 # pip3 install sklearn
import gensim.models.word2vec as w2v    # pip3 install gensim
import pandas as pd                     # pip3 install pandas
import seaborn as sns                   # pip3 install seaborn

MOST_SIMILAR = "MOST_SIMILAR"   # model.wv.most_similar(positive=["homer"]))
GET_VECTOR = "GET_VECTOR"       # model.wv.get_vector(key)

def QueryModel(model_name, command, query):
  model = w2v.Word2Vec.load(os.path.join("models", model_name))

  if command == MOST_SIMILAR:
    return model.wv.most_similar(query)
  
  if command == GET_VECTOR:
    return model.wv.get_vector(query)

  return
