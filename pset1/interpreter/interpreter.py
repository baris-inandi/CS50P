a = input("Expression: ")

split = a.split(" ")
x = float(split[0])
op = split[1]
y = float(split[2])

if op == "+":
    print(x+y)
elif op == "-":
    print(x-y)
elif op == "*":
    print(x*y)
elif op == "/":
    print(x/y)
