import re


def main():
    print(count(input("Text: ")))


def count(s):
    r = r"(^|\W)um($|\W)"
    return len(re.findall(r, s, re.IGNORECASE))


if __name__ == "__main__":
    main()
