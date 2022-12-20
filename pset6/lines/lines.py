import sys
from sys import argv


def main():
    if len(argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    if not argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(1)

    try:
        with open(argv[1]) as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

    print(
        len(
            list(
                filter(
                    lambda line: line.strip() != ""
                    and not line.strip().startswith("#"),
                    lines,
                )
            )
        )
    )


if __name__ == "__main__":
    main()
