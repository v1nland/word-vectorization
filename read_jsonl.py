# run as: python3 read_jsonl.py data/example.jsonl corpus/example.corpus

import sys
import json
import re
from helper.utils import validateJSON
from helper.utils import checkRetweet
from helper.utils import hasData


def ReadJsonl(raw_tweets_file_name, corpus_file_name):
    raw_tweets_file = open("data/" + raw_tweets_file_name + ".jsonl", "r")
    corpus_file = open("corpus/" + corpus_file_name + ".corpus", "w+")

    # loop over json list file
    for line in raw_tweets_file:
        if validateJSON(line) == False:
            continue

        # parse as json object
        json_object = json.loads(line)

        # parse tweet to remove custom encoding (emoji, weird non-ascii chars)
        tweet = (
            json_object["full_text"].encode("ascii", "ignore").decode("ascii").split()
        )

        # if tweet couldn't be parsed, avoid it
        if tweet == [] or hasData(tweet) == False:
            continue

        # apply regex filter to each word
        tweet = [re.sub("[^A-Za-z0-9@#]+", "", word) for word in tweet]

        # remove all mentions, urls, hashtags and empty words
        tweet = [
            word.lower()
            for word in tweet
            if not (
                "@" in word
                or "http" in word
                or "#" in word
                or "" == word
                or " " == word
            )
        ]

        # check if tweet is a retweet
        if checkRetweet(tweet):
            continue

        # tweet is an array
        # tweet[i] is a word
        if hasData(tweet):
            tweet.append("\n")
            corpus_file.write(" ".join([str(elem) for elem in tweet]))

    raw_tweets_file.close()
    corpus_file.close()


def main():
    if len(sys.argv) < 3:
        print(
            "correct usage: python3 read_jsonl.py <input_raw_tweets_file_name> <output_corpus_file_name>"
        )
        return

    RAW_TWEETS_FILE_NAME = sys.argv[1]
    CORPUS_FILE_NAME = sys.argv[2]

    # process input data and save it to file
    ReadJsonl(RAW_TWEETS_FILE_NAME, CORPUS_FILE_NAME)


if __name__ == "__main__":
    main()
