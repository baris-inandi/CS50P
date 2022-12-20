def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def ends_with_nums(s):
    if s.isalpha():
        return True
    for i, c in enumerate(s):
        if c.isnumeric():
            return "".join(list(s)[i:]).isnumeric()
    return False


def first_num_non_zero(s):
    for c in s:
        if c.isnumeric():
            if c == "0":
                return False
            return True
    return True


def is_valid(s):
    return (
        s.isalnum()  # all alphanumeric
        and len(s) >= 2  # length between 2
        and len(s) <= 6  # and 6
        and s[:2].isalpha()  # first two chars should be letters
        and first_num_non_zero(s)  # first number shouldn't be 0
        and ends_with_nums(s)  # should end with numbers or have no numbers at all
    )


if __name__ == "__main__":
    main()
