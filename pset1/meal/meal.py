def main():
    ...


def convert(time):
    split = time.strip().split(":")
    # separate hours and minutes
    hours = int(split[0])
    minutes = int(split[-1])
    # find out which minute of the day we are looking for
    hours*60 + minutes



if __name__ == "__main__":
    main()
