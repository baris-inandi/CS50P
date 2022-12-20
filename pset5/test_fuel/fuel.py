def convert(fraction):
    split = fraction.split("/")
    x, y = split[0], split[1]
    percentage = round(int(x) / int(y) * 100)
    if percentage > 100:
        raise ValueError("x should be <= y")
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    return f"{str(percentage)}%"


def main():
    try:
        print(gauge(convert(input("Fraction: "))))
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
