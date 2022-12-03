import inflect

names = []

try:
    while True:
        i = input("Name: ")
        names.append(i)
except EOFError:
    print()
    p = inflect.engine()
    print("Adieu, adieu, to", p.join((names)))
