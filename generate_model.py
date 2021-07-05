# run as: python3 generate_model.py corpus/example.corpus models/example.w2v

import sys
import multiprocessing
import gensim.models


def GenerateModel(corpus_file_name, model_file_name):
    corpus_file = open("corpus/" + corpus_file_name + ".corpus", "r")
    corpus_sentences = corpus_file.readlines()
    corpus = [line.split() for line in corpus_sentences]

    print("Corpus length: ", len(corpus))

    print("GenerateModel has begun...")

    cores = multiprocessing.cpu_count()

    model = gensim.models.Word2Vec(
        sentences=corpus,
        min_count=5,
        vector_size=200,  # change for 300
        workers=cores - 1,
    )

    print("Model: ", model)

    print("Training has begun. This process may take a few minutes. Be patient...")

    model.train(corpus, total_examples=model.corpus_count, epochs=30, report_delay=1)

    print("Training complete!")

    model.save("models/" + model_file_name + ".w2v")

    print("Your trained model was saved as: models/" + model_file_name + ".w2v")


def main():
    if len(sys.argv) < 3:
        print(
            "correct usage: python3 generate_model.py <input_corpus_file_name> <output_model_file_name>"
        )
        return

    CORPUS_FILE_NAME = sys.argv[1]
    MODEL_FILE_NAME = sys.argv[2]

    # generate w2v model
    GenerateModel(CORPUS_FILE_NAME, MODEL_FILE_NAME)


if __name__ == "__main__":
    main()
