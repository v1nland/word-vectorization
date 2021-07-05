# run as: python3 shuffle_set.py earthquake_hurricane earthquake_hurricane

import random
import sys


def ShuffleSet(set_file, shuffled_set_name):
    with open("set/" + set_file + ".set", "r") as source:
        data = [(random.random(), line) for line in source]

    data.sort()

    with open("shuffled_set/" + shuffled_set_name + ".shuffled_set", "w") as target:
        for _, line in data:
            target.write(line)


def main():
    if len(sys.argv) < 3:
        print("correct usage: python3 shuffle_set.py <set_name> <shuffled_set_name>")
        return

    SET_NAME = sys.argv[1]
    SHUFFLED_SET_NAME = sys.argv[2]

    ShuffleSet(SET_NAME, SHUFFLED_SET_NAME)


if __name__ == "__main__":
    main()
