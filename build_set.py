# run as: python3 build_set.py \[\'earthquake\',\'hurricane\'\] 5 TRAIN

import sys


def BuildSet(corpus_files, tweets_number):
    with open("set/" + "_".join(corpus_files) + ".set", "w") as out_file:
        for file_index, file in enumerate(corpus_files):
            with open("corpus/" + file + ".corpus") as in_file:
                counter = 0

                for line in in_file:
                    if counter >= tweets_number and tweets_number != 0:
                        break

                    line = line.replace(" \n", "")
                    out_file.write(
                        '{{"type":{0},"data":"{1}"}}\n'.format(file_index, line)
                    )
                    counter = counter + 1


def main():
    if len(sys.argv) < 3:
        print(
            "correct usage: python3 build_set.py <input_corpus_file_names> <tweets_number>"
        )
        return

    CORPUS_FILES = eval(sys.argv[1])
    TWEETS_NUMBER = int(sys.argv[2])

    BuildSet(CORPUS_FILES, TWEETS_NUMBER)


if __name__ == "__main__":
    main()
