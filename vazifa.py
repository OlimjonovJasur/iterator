"""  Fibonacci sonlarini iterator orqali chiqaring  """

class Fibolar:
    def __init__(self, limit: int):
        self.a = 0
        self.b = 1
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return current


fib = Fibolar(20)
for num in fib:
    print(num)
