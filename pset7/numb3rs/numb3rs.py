import sys
import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    try:
        split = ip.split(".")
        if len(split) != 4:
            return False
        for octet in split:
            if not 0 <= int(octet) <= 255:
                return False
    except ValueError:
        return False
    return True


if __name__ == "__main__":
    main()
