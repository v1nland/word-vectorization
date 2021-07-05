# run as: python3 join_files.py \[\'file_1\',\'file_2\'\]

import sys
from helper.utils import validateJSON


def JoinFiles(files):
    # Open output file in write mode
    with open("data/" + "_".join(files) + ".jsonl", "w") as out_file:

        # Iterate through files list
        for file in files:

            # Open each file in read mode
            with open("data/" + file + ".jsonl") as in_file:

                for line in in_file:

                    # read the data from files and write it in file3
                    if validateJSON(line):
                        out_file.write(line)


def main():
    if len(sys.argv) < 2:
        print("correct usage: python3 join_files.py \[\\'file_1\\',\\'file_2\\'\]")
        return

    FILES = eval(sys.argv[1])

    JoinFiles(FILES)


if __name__ == "__main__":
    main()
