import json
import re

def ReadJsonl(lines):
  tweets = []

  # loop over json list file
  for line in lines:
    # parse as json object
    json_object = json.loads(line.strip())

    # parse tweet to remove custom encoding (emoji, weird non-ascii chars)
    tweet = json_object["full_text"].encode('ascii', 'ignore').decode('ascii').split()

    # if tweet couldn't be parsed, avoid it
    if tweet == [] or TweetHasData(tweet) == False:
      continue

    # apply regex filter to each word
    tweet = [re.sub('[^A-Za-z0-9@#]+', '', word) for word in tweet]

    # remove all mentions, urls, hashtags and empty words
    tweet = [word for word in tweet if not ("@" in word or "http" in word or "#" in word or "" == word or " " == word)]

    # check if tweet is a retweet
    if CheckRetweet(tweet):
      continue
    
    # tweets[i] is an array
    # tweets[i][j] is a word
    if TweetHasData(tweet):
      tweet.append("\n")
      tweets.append(tweet)

  return tweets

def CheckRetweet(tweet):
  for word in tweet:
    word = word.lower()

    if word == "rt":
      return True

  return False

def TweetHasData(tweet):
  for word in tweet:
    if word != "" and word != " ":
      return True

  return False
