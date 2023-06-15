import os

current_path = os.path.abspath(__file__)

parrent_path = os.path.join(current_path, '..', '..')

print(current_path)

print(parrent_path)

def recurs(count):
    print(count)
    if count == 5:
        return
    recurs(count+1)
    print(count)

def get_all_files(path)
for i_name in os.listdir(path):
    new_path = os.path.join(path, i_name)
    if os.path.isdir(new_path):
        print('fk', i_name)
        get_all_files(path)
    else:
        print('-', i_name)

get_all_files(parrent_path)
