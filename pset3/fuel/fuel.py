def get_fuel():
    fraction = input("Fraction: ")
    split = fraction.split("/")
    x, y = split[0], split[1]
    percentage = round(int(x) / int(y) * 100)
    if percentage > 100:
        raise ValueError("x should be <= y")
    out = str(percentage) + "%"
    if percentage <= 1:
        out = "E"
    elif percentage >= 99:
        out = "F"
    return out


def main():
    try:
        print(get_fuel())
        return
    except ValueError:
        print("x and y should be integers where x <= y")
    except ZeroDivisionError:
        print("Tank capacity cannot be 0")
    except IndexError:
        print("Enter a valid fraction formatted as X/Y")
    main()


if __name__ == "__main__":
    main()
