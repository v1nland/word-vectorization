import os
import sys

# import gensim.models.word2vec as w2v

from helper.utils import getModelRoute

# MODEL_FILE_NAME = "models/earthquake_hurricane.w2v"

# MOST_SIMILAR = "MOST_SIMILAR"  # model.wv.most_similar(positive=["homer"]))
# GET_VECTOR = "GET_VECTOR"  # model.wv.get_vector(key)
# EXISTS = "EXISTS"


def MostSimilar(model, query):
    try:
        result = model.wv.most_similar(query)
        return result
    except:
        return []


def Vector(model, query):
    try:
        vector = model.wv.get_vector(query)
        result = [float(pos) for pos in vector]

        return result
    except:
        return []


def Exists(model, query):
    try:
        result = model.wv.get_vector(query)
        return True
    except:
        return False
