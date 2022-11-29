a = input("Expression: ")

split = a.split(" ")
x = float(split[0])
op = split[1]
y = float(split[2])

if op == "+":
    print("{:.2f}".format(x+y))
elif op == "-":
    print("{:.2f}".format(x-y))
elif op == "*":
    print("{:.2f}".format(x*y))
elif op == "/":
    print("{:.2f}".format(x/y))
