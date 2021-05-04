import json

CORPUS_FILES = ["earthquake", "hurricane"]
TWEETS_NUMBER = 0  # set to 0 for all tweets


def BuildTrainSet(corpus_files, tweets_number):
    with open("train_set/" + "_".join(corpus_files) + ".train_set", "w") as out_file:
        for file_index, file in enumerate(corpus_files):
            with open("corpus/" + file + ".corpus") as in_file:
                counter = 0

                for line in in_file:
                    if counter >= tweets_number and tweets_number != 0:
                        break

                    line = line.replace(" \n", "")
                    out_file.write('{{"type":{0},"data":"{1}"}}\n'.format(file_index, line))
                    counter = counter + 1

            


def main():
    BuildTrainSet(CORPUS_FILES, TWEETS_NUMBER)


if __name__ == "__main__":
    main()
