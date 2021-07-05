# run as: python3 parse_set.py earthquake_hurricane earthquake_hurricane 200 TEST
# run as: python3 parse_set.py earthquake_hurricane earthquake_hurricane 200 TRAIN

import sys
import json

# w2v
import gensim.models.word2vec as w2v

# project files
import query_model


def ProcessLine(model, words_per_tweet, tweet_type, tweet_data):
    if len(tweet_data) < words_per_tweet:
        while len(tweet_data) < words_per_tweet:
            tweet_data.append("")
    else:
        del tweet_data[words_per_tweet:]

    tweet_words_data = []
    for word in tweet_data:
        if query_model.Exists(model, word):
            word_vector = query_model.Vector(model, word)
            tweet_words_data.append({"word": word, "vector": word_vector})
        else:
            word_vector = [0] * 200
            tweet_words_data.append({"word": word, "vector": word_vector})

    return tweet_type, tweet_words_data


def ParseSet(
    shuffled_set_file_name, vectorizated_set_name, w2v_model_file_name, words_per_tweet
):
    model = w2v.Word2Vec.load("models/" + w2v_model_file_name + ".w2v")
    shuffled_set_file = open(
        "shuffled_set/" + shuffled_set_file_name + ".shuffled_set", "r"
    )

    with open(
        "vectorizated_shuffled_set/"
        + vectorizated_set_name
        + ".vectorizated_shuffled_set",
        "w",
    ) as out_file:
        for line in shuffled_set_file:
            json_object = json.loads(line)

            tweet_type, tweet_words_data = ProcessLine(
                model, words_per_tweet, json_object["type"], json_object["data"].split()
            )

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
    if len(sys.argv) < 5:
        print(
            "correct usage: python3 parse_set.py <shuffled_set_name> <vectorizated_set_name> <w2v_model_name> <words_per_tweet>"
        )
        return

    SHUFFLED_SET_NAME = sys.argv[1]
    VECTORIZATED_SET_NAME = sys.argv[2]
    W2V_MODEL_NAME = sys.argv[3]
    WORDS_PER_TWEET = int(sys.argv[4])

    ParseSet(SHUFFLED_SET_NAME, VECTORIZATED_SET_NAME, W2V_MODEL_NAME, WORDS_PER_TWEET)


if __name__ == "__main__":
    main()
