def main():
    print(shorten(input("")))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    # a list of characters where `c not in vowels`
    return "".join(c for c in word if c.lower() not in vowels)


if __name__ == "__main__":
    main()
