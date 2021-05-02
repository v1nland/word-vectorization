import os
import multiprocessing
import gensim.models  # pip3 install gensim

CORPUS_FILE_NAME = "corpus/example.corpus"
MODEL_FILE_NAME = "models/example.w2v"


def GenerateModel(corpus_file_name, model_file_name):
    corpus_file = open(corpus_file_name, "r")
    corpus_sentences = corpus_file.readlines()
    corpus = [line.split() for line in corpus_sentences]

    print("Corpus length: ", len(corpus))

    print("GenerateModel has begun...")

    cores = multiprocessing.cpu_count()

    model = gensim.models.Word2Vec(
        sentences=corpus,
        min_count=5,
        vector_size=200,
        workers=cores - 1,
    )

    print("Model: ", model)

    print("Training has begun. This process may take a few minutes. Be patient...")

    model.train(corpus, total_examples=model.corpus_count, epochs=30, report_delay=1)

    print("Training complete!")

    model.save(model_file_name)

    print("Your trained model was saved as: " + model_file_name)


def main():
    # generate w2v model
    GenerateModel(CORPUS_FILE_NAME, MODEL_FILE_NAME)


if __name__ == "__main__":
    main()
