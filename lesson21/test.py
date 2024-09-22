# класи
from pathlib import Path


class User:
    """Class User"""
    name = 'Oleksandr'
    age = 19


user1 = User()
print(user1.name)
print(user1.age)

user2 = User()
user2.name = 'Masha'
user2.age = 18
print(user2.name)
print(user2.age)


class User:
    name = 'Oleksandr'
    age = 19

    def say_name(self):
        print(f'Hi I am {self.name} and I am {self.age} years old')

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name


bob = User()
bob.set_name('Bob')
bob.say_name()

bob.set_age(18)
bob.say_name()


class Human:
    name = ''

    def hello(self, value):
        if self.name:
            return f'Hello {value} I am {self.name}'
        return f'Hello {value}'


bob = Human()
print(bob.hello('Bill'))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f'Hi {self.name}'


p = Person('Oleksandr', 19)
print(p.name)
print(p.age)
print(p.greeting())


class Person:
    name: str
    age: int

    def greeting(self):
        return f'Hi {self.name}'


p = Person()
p.name = 'Oleksandr'
print(p.greeting())


class Human:
    name = ''

    def voice(self):
        return f'Hello! My name is {self.name}'


class Developer(Human):
    field_description = 'My programming language'
    language = ''
    a = 'hft'

    def make_some_code(self):
        return f'{self.field_description} is {self.language}'


class A(Human):
    field_description = 'My'


class B(Human):
    field_description = 'Mydwa'


class C(Human):
    field_description = 'Myth'
    a = 'dwa'


class D(Human):
    field_description = 'Myjf'


class PythonDeveloper(C, Developer, A, B, D):
    language = 'Python'


class JSDeveloper(Developer):
    language = 'JS'


python_dev = PythonDeveloper()
python_dev.name = 'Oleksandr'
print(python_dev.language)
print(python_dev.c)
print(python_dev.field_description)
print(python_dev.make_some_code())
print(python_dev.voice())

js_dev = JSDeveloper()
js_dev.name = 'Slava'
print(js_dev.language)
print(js_dev.make_some_code())
print(js_dev.voice())

# MRO
