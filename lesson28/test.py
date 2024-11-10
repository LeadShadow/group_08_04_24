# ціна == якість
# ціна < якість
from math import pi


# SOLID
# Single responsibility
# Open-Closed
# Liskov substitution
# Interface segregation
# Dependency inversion


# Single responsibility -> принцип єдиної відповідальності
# поганий приклад
class Person:
    def __init__(self, name, zip, city, street):
        self.name = name
        self.zip = zip
        self.city = city
        self.street = street

    def get_address(self):
        return f'{self.zip}, {self.city}, {self.street}'


person = Person('Oleksandr', '36007', 'Kyiv', 'Vigovsokogo 18')
print(person.get_address())


# з використанням Single responsibility
class PersonAddress:
    def __init__(self, zip, city, street):
        self.zip = zip
        self.city = city
        self.street = street

    def get_address(self):
        return f'{self.zip}, {self.city}, {self.street}'


class Person:
    def __init__(self, name, address: PersonAddress):
        self.name = name
        self.address = address

    def get_address(self):
        return self.address.get_address()


person = Person('Oleksandr', PersonAddress('36007', 'Kyiv', 'Vigovsokogo 18'))
print(person.get_address())


# Open-Closed -> принцип відкритості/закритості
class Figure:
    def total_area(self):
        pass


class Rect(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    # def total_area(self):


def total_area(shapes):
    sum_ = 0
    for el in shapes:
        if isinstance(el, Rect):
            sum_ += el.width * el.height
        elif isinstance(el, Circle):
            sum_ += el.radius ** 2 * pi
    return sum_


shapes = [Rect(10, 10), Rect(4, 5), Rect(3, 3), Circle(5), Circle(3)]
area = total_area(shapes)
print(area)


class Figure:
    def total_area(self):
        pass


class Rect(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def total_area(self):
        return self.height * self.width


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def total_area(self):
        return self.radius ** 2 * pi


def total_area(shapes):
    sum_ = 0
    for el in shapes:
        sum_ += el.total_area()
    return sum_


shapes = [Rect(10, 10), Rect(4, 5), Rect(3, 3), Circle(5), Circle(3)]
area = total_area(shapes)
print(area)


# Interface segregation -> принцип розділення інтерфейсу

# поганий приклад
class Programmer:
    def write_code(self):
        pass

    def eat_pizza(self, slice_count):
        pass


class OfficeProgrammer(Programmer):
    def __init__(self, name):
        self.name = name

    def eat_pizza(self, slice_count):
        print(f'{self.name} eat {slice_count} slice pizza!')

    def write_code(self):
        print(f'{self.name} write code!')


class RemoteProgrammer(Programmer):
    def __init__(self, name):
        self.name = name

    def write_code(self):
        print(f'{self.name} write code!')


office_worker = OfficeProgrammer('Oleksandr')
office_worker.write_code()
office_worker.eat_pizza(3)


class CodeProducer:
    def write_code(self):
        pass


class PizzaConsumer:
    def eat_pizza(self, slice_count):
        pass


class OfficeProgrammer(CodeProducer, PizzaConsumer):
    def __init__(self, name):
        self.name = name

    def eat_pizza(self, slice_count):
        print(f'{self.name} eat {slice_count} slice pizza!')

    def write_code(self):
        print(f'{self.name} write code!')


class RemoteProgrammer(CodeProducer):
    def __init__(self, name):
        self.name = name

    def write_code(self):
        print(f'{self.name} write code!')


office_worker = OfficeProgrammer('Oleksandr')
office_worker.write_code()
office_worker.eat_pizza(3)
