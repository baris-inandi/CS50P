def valid_input(x):
    i = input(x)
    if i in ["25", "10", "5"]:
        return i
    return None


while valid_input("Insert Coin: "):
    pass
