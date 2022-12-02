def main():
    vowels = ["a", "e", "i", "o", "u"]
    i = input("Input: ")
    # a list of characters where `c not in vowels`
    print("".join(c for c in i if c.lower() not in vowels))


if __name__ == "__main__":
    main()
