def main():
    # translate removes characters in the vowel list from the string
    print(input("Input: ").translate(None, ["a", "e", "i", "o", "u"]))


if __name__ == "__main__":
    main()
