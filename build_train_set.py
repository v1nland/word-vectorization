import json

TWEETS_NUMBER = 20
FILES = ["earthquake", "hurricane"]


def main():
    with open("train_set/" + "_".join(FILES) + ".jsonl", "w") as out_file:
        for file in FILES:
            with open("corpus/" + file + ".corpus") as in_file:
                counter = 0

                for line in in_file:
                    if counter >= TWEETS_NUMBER:
                        break

                    line = line.replace(" \n", "")
                    out_file.write('{{"type":"{0}","data":"{1}"}}\n'.format(file, line))
                    counter = counter + 1


if __name__ == "__main__":
    main()
