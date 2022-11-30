def ends_with_nums(s):
    for i, c in enumerate(s):
        if c.isnumeric():
            x = list(s)[len(c) - i:]
            print("".join(x))
            return str(list(s)[len(c) - i:]).isnumeric()
    return False


print(ends_with_nums("ABCD123"))
print(ends_with_nums("2ABC123498"))
