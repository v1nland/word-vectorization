# std
import json

# fastapi
from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel

# w2v
import gensim.models.word2vec as w2v

# project files
import query_model
from helper.utils import getModelRoute

app = FastAPI()


@app.get("/models/{model_name}/similar")
def get_most_similar(model_name: str, query: Optional[str] = None):
    model = w2v.Word2Vec.load(getModelRoute(model_name))

    result = query_model.MostSimilar(model, query)

    return {"response": result}


@app.get("/models/{model_name}/vector")
def get_vector(model_name: str, query: Optional[str] = None):
    model = w2v.Word2Vec.load(getModelRoute(model_name))

    result = query_model.Vector(model, query)

    return {"response": result}


@app.get("/models/{model_name}/exists")
def exists(model_name: str, query: Optional[str] = None):
    model = w2v.Word2Vec.load(getModelRoute(model_name))

    result = query_model.Exists(model, query)

    return {"response": result}


@app.get("/models/{model_name}/training")
def get_training_data(
    model_name: str, query: Optional[str] = None, dim: Optional[int] = 15
):
    model = w2v.Word2Vec.load(getModelRoute(model_name))
    train_file = open("train_set/" + model_name + ".train_set", "r")

    result = []
    for line in train_file:
        json_object = json.loads(line)

        tweet_type = json_object["type"]
        tweet_data = json_object["data"].split()

        if len(tweet_data) < dim:
            while len(tweet_data) < dim:
                tweet_data.append("")
        else:
            del tweet_data[dim:]

        tweet_words_data = []
        for word in tweet_data:
            if query_model.Exists(model, word):
                word_vector = query_model.Vector(model, word)
                tweet_words_data.append({"word": word, "vector": word_vector})
            else:
                word_vector = [0] * 200
                tweet_words_data.append({"word": word, "vector": word_vector})

        result.append(
            {
                "type": tweet_type,
                "words": len(tweet_words_data),
                "data": tweet_words_data,
            }
        )

    return {"response": result}


class GetTweetRequest(BaseModel):
    tweet: List[str]


@app.post("/models/{model_name}/tweet")
def exists(model_name: str, req: GetTweetRequest, dim: Optional[int] = 15):
    result = []

    for word in req.tweet:
        if query_model.Exists(model_name, word):
            word_vector = query_model.Vector(model_name, word)
            result.append(word_vector)
        else:
            word_vector = [0] * 200
            result.append(word_vector)

    while len(result) < dim:
        result.append([0] * 200)

    return {"dim": len(result), "tweets": result}
