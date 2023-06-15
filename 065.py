'''ml = [1,2,3,4,5]
mle = iter(ml)
print(next(mle))
print(next(mle))
print(next(mle))
print(next(mle))
print(next(mle))

for i in mle:
    print(i)

print(next(mle))'''
import random
s = int(input())
class Rad:
    def __init__(self, limit):
        self.limit = limit
    def __iter__(self):
        return self
    def __next__(self):
        if self.limit == 0:
            raise StopIteration
        self.limit -= 1
        return random.randint(0, 100)

rand_iter = Rad(s)
print(iter(rand_iter))

for i in rand_iter:
    print(i)
