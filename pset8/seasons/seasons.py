import operator
import sys
from datetime import date

import inflect

p = inflect.engine()


def main():
    try:
        d = date.fromisoformat(input("Date of Birth: "))
        diff = operator.sub(date.today(), d)
        print(convert(diff.days))
    except ValueError:
        sys.exit("Invalid date")


def convert(time):
    mins = 60 * 24 * time
    mins_repr = str((p.number_to_words(mins, andword="")).capitalize())
    return mins_repr + " minutes"


if __name__ == "__main__":
    main()
