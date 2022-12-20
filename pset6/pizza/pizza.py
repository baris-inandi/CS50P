from sys import argv
import sys
from tabulate import tabulate
import csv


def main():
    if len(argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    if not argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)

    try:
        with open(argv[1]) as file:
            result_list = list(csv.reader(file))
            print(tabulate(result_list[1:], headers=result_list[0], tablefmt="grid"))
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


if __name__ == "__main__":
    main()
