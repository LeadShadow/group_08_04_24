import pickle
import json
import csv
expences = {
    'hotel': 1000,
    'breakfast': 200,
    'taxi': 200,
    'lunch': 150,
}

file_name = 'expences.txt'
with open(file_name, 'w') as file:
    for key, value in expences.items():
        file.write(f'{key}|{value}\n')


expences = {}
with open(file_name, 'r') as file:
    raw_expences = file.readlines()
    print(raw_expences)
    for line in raw_expences:
        key, value = line.split('|')
        value = value.replace('\n', '')
        print(key, value)
        expences[key] = int(value)

print(expences)

print('-------------------------------------')
some_data = {
    (1, 3.5): 'tuple',
    2: [1, 2, 3],
    'a': {'key': 'value'}
}

file_name = 'data.bin'

with open(file_name, 'wb') as file:
    pickle.dump(some_data, file)


with open(file_name, 'rb') as file:
    unpacked = pickle.load(file)


print(some_data == unpacked)
print(unpacked)

# dumps, loads


class Human:
    def __init__(self, name):
        self.name = name


sasha = Human('Sasha')
print(sasha.name)

with open(file_name, 'wb') as file:
    pickle.dump(sasha, file)


with open(file_name, 'rb') as file:
    unpacked = pickle.load(file)


print(sasha.name == unpacked.name)
print(unpacked.name)
print(sasha.name)

# json
# backend(обробляє фільтр) -> frontend(відмальовуються всі товари)
some_data = {
    'key': 'value',
    2: [1, 2, 3],
    'tuple': (5, 6),
    'a': {'key': 'value'}
}
file_name = 'test.json'
with open(file_name, 'w') as file:
    json.dump(some_data, file)


with open(file_name, 'r') as file:
    unpacked = json.load(file)


print(some_data)
print(unpacked)

# Повномасштабна війна в Україні - 24 лютого 2022 року
#
