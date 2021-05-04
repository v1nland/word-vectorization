import json

# w2v
import gensim.models.word2vec as w2v

# project files
import query_model

TRAIN_SET_NAME = "earthquake_hurricane"
MODEL_NAME = "earthquake_hurricane"
DIM = 10


def ParseTrainSet(train_set_file_name, model_file_name, dim):
    model = w2v.Word2Vec.load("models/" + model_file_name + ".w2v")
    train_file = open("train_set/" + train_set_file_name + ".train_set", "r")

    with open(
        "parsed_train_set/" + train_set_file_name + ".parsed_train_set", "w"
    ) as out_file:
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

            out_file.write(
                json.dumps(
                    {
                        "type": tweet_type,
                        "words": len(tweet_words_data),
                        "data": tweet_words_data,
                    }
                )
                + "\n"
            )


def main():
    ParseTrainSet(TRAIN_SET_NAME, MODEL_NAME, DIM)


if __name__ == "__main__":
    main()
