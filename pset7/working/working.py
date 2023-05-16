class WorkingTime:
    def __init__(self, t):
        t = t.strip()
        meridiem = ""
        if t.endswith(" AM") or t.endswith(" PM"):
            meridiem = t[-2:].upper()
            t = t[:-2].strip()
        split = t.split(":")
        if len(split) == 1:
            split = f"{split[0]}:00".split(":")
        try:
            split = [int(x) for x in split]
        except ValueError:
            raise ValueError("Invalid time format: time should consist of integers")
        if split[0] < 0 or split[0] > 12:
            raise ValueError("Invalid time format: input hour must be between 0 and 12")
        if meridiem == "PM" and split[0] != 12:
            split[0] += 12
        if meridiem == "AM" and split[0] == 12:
            split[0] = 0
        self.hour = split[0]
        self.minute = split[1]

    def validate(self):
        if self.minute < 0 or self.minute > 59:
            raise ValueError("Invalid time format: minute must be between 0 and 59")
        if self.hour < 0 or self.hour > 23:
            raise ValueError("Invalid time format: hour must be between 0 and 23")

    def __repr__(self):
        return f"{self.hour:02}:{self.minute:02}"


def convert(s):
    try:
        split = s.split("to")
        if len(split) != 2:
            raise ValueError(
                "Invalid time format: use 'to' to separate start and end times"
            )
        start = split[0].strip()
        end = split[1].strip()
        start = WorkingTime(start)
        end = WorkingTime(end)
        start.validate()
        end.validate()
        return f"{start} to {end}"
    except IndexError:
        raise ValueError("Invalid time format: must be in valid format")


def main():
    print(convert(input("Hours: ")))


if __name__ == "__main__":
    main()
