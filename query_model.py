import os
import sys
import gensim.models.word2vec as w2v  # pip3 install gensim

MODEL_FILE_NAME = "models/earthquake_hurricane.w2v"

MOST_SIMILAR = "MOST_SIMILAR"  # model.wv.most_similar(positive=["homer"]))
GET_VECTOR = "GET_VECTOR"  # model.wv.get_vector(key)


def QueryModel(model_name, command, query):
    model = w2v.Word2Vec.load(model_name)

    if command == MOST_SIMILAR:
        return model.wv.most_similar(query)

    if command == GET_VECTOR:
        return model.wv.get_vector(query)

    return


def main():
    if len(sys.argv) < 2:
        print("You need to specify command and query args")
        return

    command = sys.argv[1]
    query = sys.argv[2]

    result = QueryModel(MODEL_FILE_NAME, command, query)

    print(result)


if __name__ == "__main__":
    main()
