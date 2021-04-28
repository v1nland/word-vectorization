import json

FILES = ["earthquake", "hurricane"]


def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True


def main():
    # Open output file in write mode
    with open("data/" + "_".join(FILES) + ".jsonl", "w") as out_file:

        # Iterate through files list
        for file in FILES:

            # Open each file in read mode
            with open("data/" + file + ".jsonl") as in_file:

                for line in in_file:

                    # read the data from files and write it in file3
                    if validateJSON(line):
                        out_file.write(line)


if __name__ == "__main__":
    main()
