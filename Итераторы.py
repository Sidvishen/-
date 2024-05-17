class EvenNumbers:
    def __init__(self, max):
        self.max = max
        self.current = 10
        self.even = [10, 25]

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            result = self.current
            self.current += 2
            return result
        else:
            raise StopIteration

en = EvenNumbers(25)
for i in en:
    print(i)


