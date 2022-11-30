def main():
    vowels = ["a", "e", "i", "o", "u"]
    i = input("Input: ")
    #
    print("".join(c for c in i if c not in vowels))


if __name__ == "__main__":
    main()
