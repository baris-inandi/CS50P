def main():
    out = ""
    for char in input("camelCase: "):
        # loop over each character
        if char.isupper():
            # append an underscore and `char.lower()`
            # if `char` is capital
            out += "_" + char.lower()
            continue
        # otherwise, just continue appending
        out += char
    print(f"snake_case: {out}")


if __name__ == "__main__":
    main()
