import validators


def main():
    t = input("What's your email address? ")
    if validators.email(t):
        return print("Valid")
    else:
        return print("Invalid")


if __name__ == "__main__":
    main()
