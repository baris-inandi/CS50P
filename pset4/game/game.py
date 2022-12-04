import random


# only returns non-default value if prompt is an integer
def int_input(prompt: str, default: int):
    i = input(prompt)
    return int(i) if i.isnumeric() else default


# get valid input, ask for level until it is a valid int that is greater than 0
level = 0
while level <= 0:
    level = int_input("Level: ", 0)


ans = random.randint(1, level)
user_in = 0
while user_in != ans:
    user_in = int_input("Guess: ", 0)
    if user_in > ans:
        print("Too large!")
    elif user_in < ans:
        print("Too small!")
    else:
        print("Just right!")
