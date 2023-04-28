import re


def main():
    print(parse(input("HTML: ")))


def parse(s: str):
    s = s.strip()
    try:
        url = re.search('(?<=youtube\.com\/embed\/).+?(?=")', s)
        if url is not None:
            return f"https://youtu.be/{url.group(0)}"
        return None
    except Exception:
        return None


if __name__ == "__main__":
    main()
