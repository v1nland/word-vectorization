import json


def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True


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


def writeFile(file_name, content_list):
    f = open(file_name, "w", newline="")

    for tweet in content_list:
        line = " ".join([str(elem) for elem in tweet])

        f.write(line)
    f.close()


def getModelRoute(model_name):
    return "models/{}.w2v".format(model_name)