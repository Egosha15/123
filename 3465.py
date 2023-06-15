spisok = (x**2 for x in range(1000000))

def gen():
    for x in range(1000000):
        yield x**2

