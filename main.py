from generate_model import GenerateModel
from read_jsonl import ReadJsonl
from write_file import WriteFile

RAW_TWEETS_FILE_NAME = "data/earthquake_hurricane.jsonl"
CORPUS_FILE_NAME = "corpus/earthquake_hurricane.corpus"
MODEL_FILE_NAME = "models/earthquake_hurricane.w2v"


def main():
    # process input data and save it to file
    ReadJsonl(RAW_TWEETS_FILE_NAME, CORPUS_FILE_NAME)

    # generate w2v model
    GenerateModel(CORPUS_FILE_NAME, MODEL_FILE_NAME)


if __name__ == "__main__":
    main()
