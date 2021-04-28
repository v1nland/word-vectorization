import json
import re


def ReadJsonl(raw_tweets_file_name, corpus_file_name):
    raw_tweets_file = open(raw_tweets_file_name, "r")
    corpus_file = open(corpus_file_name, "w+")

    # loop over json list file
    for line in raw_tweets_file:
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


def checkRetweet(tweet):
    for word in tweet:
        word = word.lower()

        if word == "rt":
            return True

    return False


def hasData(tweet):
    for word in tweet:
        if word != "" and word != " ":
            return True

    return False
