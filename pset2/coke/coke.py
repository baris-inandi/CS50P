def valid_input(x):
    # returns the string only if it is a valid denomination
    i = input(x)
    if i in ["25", "10", "5"]:
        return i
    return None


def main():
    # define initial price of 50 cents
    due = 50
    while True:
        i = valid_input("Insert Coin: ")
        if i:
            due -= int(i)
        # ask for input
        if due <= 0:
            # if $0 or less due, stop asking for coins
            if due < 0:
                # if there is a charge owed (not 0)
                print(f"Change owed {-1*due}")
            break
        print(f"Amount due: {due}")


if __name__ == "__main__":
    main()
