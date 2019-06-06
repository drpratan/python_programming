class Counter():
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        'Returns itself as an iterator object'
        return self

    def __next__(self):
        'Returns the next value till current is lower than high'
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


c = Counter(5,10)
for i in c:
     print(i, end=' ')

d = Counter(1,4)
print ("\n " , d.__next__())
print ("\n " , d.__next__())
print ("\n " , d.__next__())
print ("\n " , d.__next__())
print ("\n " , d.__next__())
