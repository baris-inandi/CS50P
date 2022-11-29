def main():
    x = input("What time is it? ")
    if in_between(x, "7:00", "8:00"):
        print("breakfast time")
    elif in_between(x, "12:00", "13:00"):
        print("lunch time")
    elif in_between(x, "18:00", "19:00"):
        print("dinner time")


def in_between(test, start, end):
    # returns true if test (hrs) is between start and end (hrs)
    if convert(test) >= convert(start) and convert(test) <= convert(end):
        return True
    return False


def convert(time):
    # converts a time string to an integer
    # that represents hours passed after 00:00

    split = time.strip().split(":")
    # multiplies hours (at index 0) by 60
    # adds it to the seconds (at index -1)
    return int(split[0]) + int(split[-1]) / 60


if __name__ == "__main__":
    main()
