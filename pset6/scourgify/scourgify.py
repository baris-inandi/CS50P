from sys import argv
import sys
import csv


def fix_csv(data):
    out = [["first", "last", "house"]]
    for i in data[1:]:
        split = i[0].split(",")
        first = split[1].strip()
        last = split[0].strip()
        out.append([first, last, i[1]])
    return out


def main():
    if len(argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    if not (argv[1].endswith(".csv") and argv[2].endswith(".csv")):
        print("Files should be .csv")
        sys.exit(1)

    try:
        with open(argv[1]) as file:
            out = fix_csv(list(csv.reader(file)))
        with open(argv[2], "w+") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(out)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


if __name__ == "__main__":
    main()
