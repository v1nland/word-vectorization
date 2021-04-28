import os
import multiprocessing
import gensim.models.word2vec as w2v  # pip3 install gensim


def GenerateModel(corpus_file_name, model_file_name):
    corpus_file = open(corpus_file_name, "r")

    print("GenerateModel has begun...")

    cores = multiprocessing.cpu_count()

    model = w2v.Word2Vec(
        min_count=20,
        window=2,
        sample=6e-5,
        alpha=0.03,
        min_alpha=0.0007,
        negative=20,
        workers=cores - 1,
    )

    model.build_vocab(corpus_file, progress_per=10000)

    # print("Model vocabulary length: ", len(model.wv.vocab))

    print("Training has begun. This process may take a few minutes. Be patient...")

    model.train(
        corpus_file, total_examples=model.corpus_count, epochs=30, report_delay=1
    )

    print("Training complete!")

    model.save(model_file_name)

    print("Your trained model was saved as: " + model_file_name)

    corpus_file.close()
