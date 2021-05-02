import json
import re
from helper.utils import validateJSON
from helper.utils import checkRetweet
from helper.utils import hasData

RAW_TWEETS_FILE_NAME = "data/example.jsonl"
CORPUS_FILE_NAME = "corpus/example.corpus"


def ReadJsonl(raw_tweets_file_name, corpus_file_name):
    raw_tweets_file = open(raw_tweets_file_name, "r")
    corpus_file = open(corpus_file_name, "w+")

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
    # process input data and save it to file
    ReadJsonl(RAW_TWEETS_FILE_NAME, CORPUS_FILE_NAME)


if __name__ == "__main__":
    main()