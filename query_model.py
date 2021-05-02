import os
import sys
import gensim.models.word2vec as w2v  # pip3 install gensim

# MODEL_FILE_NAME = "models/earthquake_hurricane.w2v"

MOST_SIMILAR = "MOST_SIMILAR"  # model.wv.most_similar(positive=["homer"]))
GET_VECTOR = "GET_VECTOR"  # model.wv.get_vector(key)
EXISTS = "EXISTS"


def QueryModel(model_name, command, query):
    model = w2v.Word2Vec.load(model_name)

    if command == MOST_SIMILAR:
        return model.wv.most_similar(query)

    if command == GET_VECTOR:
        try:
            vector = model.wv.get_vector(query)
            result = [float(pos) for pos in vector]

            return {"exists": True, "dim": len(result), "result": result}
        except:
            return {"exists": False, "dim": 0, "result": []}

    if command == EXISTS:
        try:
            result = model.wv.get_vector(query)
            return True
        except:
            return False

    return
