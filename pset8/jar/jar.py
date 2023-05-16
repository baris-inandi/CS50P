class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        newamount = self.size + n
        if newamount > self.capacity:
            raise ValueError("Too many cookies!")
        self.size = newamount

    def withdraw(self, n):
        newamount = self.size - n
        if newamount < 0:
            raise ValueError("Not enough cookies!")
        self.size = newamount

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, newcapacity):
        if newcapacity <= 0:
            raise ValueError("Capacity should be a positive number!")
        self._capacity = newcapacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, newsize):
        if newsize < 0:
            raise ValueError("Size should be a positive number!")
        self._size = newsize


def main():
    jar = Jar()
    jar.deposit(6)
    print(jar)
    jar.withdraw(2)
    print(jar)
    jar.withdraw(3)
    print(jar)
    jar.deposit(4)
    print(jar)
    print(jar.size)


if __name__ == "__main__":
    main()
