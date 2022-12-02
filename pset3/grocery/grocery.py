record: dict[str, int] = {}

try:
    while True:
        item = input().upper()
        record[item] = record.get(item, 0) + 1
except EOFError:
    sortednames=sorted(record.keys(), key=lambda x:x.upper())
    for i in sortednames:
        print(record[i], i)
