import random


def main():
    level = get_level()
    score = 10
    print()
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        question = f"{x} + {y} = "
        ans = x + y
        attempts = 1
        user_ans = input(question)
        while user_ans != str(ans):
            print("EEE")
            if attempts == 3:
                score -= 1
                print(question + str(ans))
                break
            user_ans = input(question)
            attempts += 1
    print("Score:", score)


def get_level():
    level = 0
    while not (level == "1" or level == "2" or level == "3"):
        level: str = input("Level: ")
    return int(level)


def generate_integer(level):
    return random.randint(
        10 ** (level - 1) + (-1 if level == 1 else 0), 10**level - 1
    )


if __name__ == "__main__":
    main()
