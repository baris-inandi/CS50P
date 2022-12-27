from PIL import Image, ImageOps
from sys import argv
import sys


def same_extension(file1, file2):
    return file1.split(".")[-1] == file2.split(".")[-1]


def main():
    if len(argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    if not same_extension(argv[1], (argv[2])):
        print("Files should have the same extension")
        sys.exit(1)

    try:
        bg = Image.open(argv[1])
        fg = Image.open("shirt.png")
        bg = ImageOps.fit(bg, fg.size)
        bg.paste(fg, fg)
        bg.save(argv[2])
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


if __name__ == "__main__":
    main()
