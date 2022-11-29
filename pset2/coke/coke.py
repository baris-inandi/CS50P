def valid_input(x):
    # returns the string only if it is a valid denomination
    i = input(x)
    if i in ["25", "10", "5"]:
        return i
    return None


def main():
    # define initial price of 50 cents
    due = 50
    # ask for input for the first time
    i = valid_input("Insert Coin: ")
    while i:
        due -= i
        # ask for input
        print(f"Amount due: {due}")
        i = valid_input("Insert Coin: ")

    if due < 0:
        print(f"Change owed {-1*due}")


if __name__ == "__main__":
    main()
