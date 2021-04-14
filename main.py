from generate_model import GenerateModel
from read_jsonl import ReadJsonl
from write_file import WriteFile

FILE_NAME = 'data/earthquake.jsonl'
OUTPUT_FILE_NAME = 'corpus/earthquake.csv'
OUTPUT_MODEL = 'models/earthquake.w2v'

def main():
  # read input data
  data = open(FILE_NAME, 'r')
  lines = data.readlines()

  # process input data
  tweets = ReadJsonl(lines)

  # write output to file
  WriteFile(OUTPUT_FILE_NAME, tweets)

  # generate w2v model
  GenerateModel(tweets, OUTPUT_MODEL)


if __name__ == "__main__":
  main()
