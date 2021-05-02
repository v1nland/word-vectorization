from typing import Optional
from fastapi import FastAPI
from query_model import QueryModel

app = FastAPI()


@app.get("/models/{model_name}/{command}")
def query_model(model_name: str, command: str, query: Optional[str] = None):
    model_file_name = "models/{}.w2v".format(model_name)

    result = QueryModel(model_file_name, command, query)

    return {"response": result}
