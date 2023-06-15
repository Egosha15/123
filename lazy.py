import time
import contextlib

'''#Обозначим строгие вычисления
my_iter = [time.sleep(x) for x in range (1,3)]
print(my_iter)

#Ленивые вычисления

my_iter2 = (time.sleep(x) for x in range (1,3))
print(my_iter2)'''

'''#Ленивые вычисления в виде функции
def lazy(items):
    for item in items:
        yield item
    yield from items

items = ['Яблоко', 'Банан', 'Груша']

for i in lazy(items):
    print (i)'''

'''file = open('54.txt', 'w')
file.write('ABOBUS')
file.close()'''

'''#Контекстный менеджер

with open('54.txt', 'w') as file:
    file.write('Sigma')
    print(file.closed) #false

print(file.closed) #true '''

#Контекстный менеджер для переворачивания строки (реверс)
@contextlib.contextmanager
def rev(str):
    print('Входим в контекстный менеджер:')
    yield str[::-1]
    print('Выходим из контекстного менеджера')
with rev('Sigma') as reversed_str:
    print(f'Выполняется код {reversed_str}')



    
