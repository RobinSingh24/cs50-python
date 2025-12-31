class Jar:
    cookies = 0
    def __init__(self, capacity=12):
        if(capacity<=0):
            raise ValueError('Invalid capacity')
        self._capacity = capacity

    def __str__(self):
        return '🍪'*self.size

    def deposit(self, n):
        if(self.size + n > self.capacity):
            raise ValueError('Capacity exceeded')
        self.cookies += n

    def withdraw(self, n):
        if(n > self.size):
            raise ValueError('Not enough cookies')
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies

def main():
    jar = Jar()
    print(jar)

if __name__ == "__main__":
    main()
