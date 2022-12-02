months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}


def validate(year, month, day):
    month, day = int(month), int(day)
    return (month >= 1 and month <= 12) and (day >= 1 and day <= 31) and year.isnumeric()


def transform_month(month):
    if month in months.keys():
        return months.get(month)
    raise ValueError("Cannot transform month string to month number")


def main():
    while True:
        try:
            date = input("Date: ").strip()
            year, month, day = "", 0, 0
            slash_split, space_split = date.split("/"), date.split(" ")

            if len(slash_split) == 3:
                # MM/DD/YYYY
                month, day, year = slash_split
            elif len(space_split) == 3:
                # MSTRING DD YYYY
                month, day, year = space_split
                if not "," in day:
                    continue
                day = day.replace(",", "")
                month = transform_month(month)

            if not validate(year, month, day):
                continue
            print(f"{year}-{int(month):02}-{int(day):02}")
            break
        except Exception:
            continue


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        pass
