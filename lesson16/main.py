# генерація випадкових чисел
import random
import collections

print(random.randint(1, 1000))
print(random.random())

# 6 6 6 6 7 7 7 7 8 8 8 8
coloda = [6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'В1', 'B2', 'B3', 'B4']
random.shuffle(coloda)
print(coloda)

fruits = ['apple', 'peach', 'banana']
print(random.choice(fruits))

fruits = ['apple', 'peach', 'banana']
print(random.choices(fruits, k=10))


fruits = ['apple', 'peach', 'banana']
print(random.sample(fruits, k=2))

# колекції
person = ('Oleksandr', 'Samus', 19)

Person = collections.namedtuple('Person', ['name', 'last_name', 'age'])
person1 = Person('Oleksandr', 'Samus', 19)
print(person1)
print(person1.name)
print(person1.last_name)
print(person1.age)
person2 = Person('Roma', 'Ovadchyk', 15)
print(person2.name)
print(person2.last_name)
print(person2.age)
some_person = {
    'name': 'Oleksandr',
    'last_name': 'Samus',
    'age': 19
}
print(some_person['name'])
print(some_person['last_name'])
print(some_person['age'])
some_person = {
    'name': 'Oleksandr',
    'last_name': 'Samus',
    'age': 19
}