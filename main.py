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
from vectorizate_set import ProcessLine

app = FastAPI()

# w2v endpoints
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


# custom endpoints
class GetTweetRequest(BaseModel):
    tweet_type: int
    tweet_data: str


@app.post("/models/{model_name}/tweet")
def exists(model_name: str, req: GetTweetRequest, words_per_tweet: Optional[int] = 16):
    model = w2v.Word2Vec.load(getModelRoute(model_name))

    tweet_type, tweet_words_data = ProcessLine(
        model, words_per_tweet, req.tweet_type, req.tweet_data.split()
    )

    return {
        "type": tweet_type,
        "words": len(tweet_words_data),
        "data": tweet_words_data,
    }
