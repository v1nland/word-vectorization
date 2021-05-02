from utils import validateJSON

TWEETS_NUMBER = 20
FILES = ["earthquake", "hurricane"]


def main():
    with open("data/first_" + "_".join(FILES) + ".jsonl", "w") as out_file:
        for file in FILES:
            with open("data/" + file + ".jsonl") as in_file:
                counter = 0

                for line in in_file:
                    if counter >= TWEETS_NUMBER:
                        break

                    if validateJSON(line):
                        out_file.write(line)
                        counter = counter + 1


if __name__ == "__main__":
    main()
