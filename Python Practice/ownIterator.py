class TheIterator:
    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > 5:
            return StopIteration
        else:
            result = self.current
            self.current += 1
            return result

iterator = TheIterator()

print(next(iterator))
print(next(iterator))
print(next(iterator))