from pprint import pprint
from typing import Iterator

goods = [
    {
        'name': 'Iphone 14',
        'brand': 'Apple',
        'price': 1200,
    },
    {
        'name': 'Samsung A53',
        'brand': 'Samsung',
        'price': 500,
    },
    {
        'name': 'Xiaomi A8',
        'brand': 'Xiaomi',
        'price': 400,
    }
]

'''def item_price(item):
    return item['price']

print(sorted(goods, key=item_price))
#сортировка по цене:
pprint(sorted(goods, key=lambda item: item['price'] ))

apple_list = list(filter(lambda item: item['brand'] == 'Apple', goods))
#проверка итератор ли это:
pprint(isinstance(apple_list, Iterator))
pprint(apple_list)'''

'''#позволяет применить действия ко всем элементам
numbers_list = ['1', '2', '3', '4', '5']
numbers_list = list(map(int, numbers_list))
print(numbers_list)

names_list = ['Ivan', 'Lena', 'Nikita', 'Oleg']
surnames_list = ['Ohlobisten', 'Golovach', 'Jigurda', 'Saldo']

full_name_list = list(map(lambda name, surname: f'{name} {surname}', names_list, surnames_list))
print(full_name_list)'''

'''index_goods = []

for i, item in enumerate(goods):
    index_goods.append({i:item})

pprint(index_goods)'''

'''names_list = ['Ivan', 'Lena', 'Nikita', 'Oleg']
surnames_list = ['Ohlobisten', 'Golovach', 'Jigurda', 'Saldo']

for name, surname in zip(names_list, surnames_list):
    print(name, surname)'''

apple_list = list(filter(lambda item: item['brand'] == 'Apple', goods))
print(apple_list)

