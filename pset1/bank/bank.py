i = input("Greeting: ").strip().lower()

if i.startswith("hello"):
    print("$0")
elif i.startswith("h"):
    print("$20")
else:
    print("$100")