'''import time
import random

class Running:
    def __init__(self):
        self.start = None
    def __enter__(self):
        self.start = time.time()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        t = time.time() - self.start
        print(f'Время работы кода: {t} сек.')

        if exc_type is TypeError:
            return True
            


with Running():
    my_list = [x for x in range(10000000)]
    my_list -= 's''''
ml = [1,2,3,4,5]
mle = iter(ml)
print(next(mle))

