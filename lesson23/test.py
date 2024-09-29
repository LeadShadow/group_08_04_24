# Магічні методи

print(10 + 20)
print('hello ' + 'world')

# a = 10
# b = 20
# print(a.__add__(b))
# print(a.__sub__(b))


class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def say_hello(self):
        return f'Hello! I am {self.name}'


bill = Human('Bill', 20)
print(bill.say_hello())


# __str__, __repr__
print([1, 2])


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __repr__(self):
    #     return f'Point {self.x}, {self.y}'

    def __str__(self):
        return f'Point {self.x}, {self.y}'

    # def print_points(self):
    #     return f'Point {self.x}, {self.y}'


p = Point(10, 20)
print(p)


# __getitem__, __setitem__
dict1 = {'1': 2}
print(dict1['1'])
dict1['2'] = 3
print(dict1['2'])


class ListedValuesDict:
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key].append(value)
        else:
            self.data[key] = [value]

    def __getitem__(self, key):
        result = str(self.data[key][0])
        for value in self.data[key][1:]:
            result += ', ' + str(value)
        return result


l_dict = ListedValuesDict()
l_dict[1] = 'a'
l_dict[1] = 'b'
print(l_dict[1])
l1_dict = {}
l1_dict[1] = 'a'
l1_dict[1] = 'b'
print(l1_dict[1])

# функтори, метод __call__


class Adder:
    def __init__(self, value):
        self.value = value

    def __call__(self, value):
        return self.value + value


two_adder = Adder(2)
print(two_adder(5))

# створення власних менеджерів контексту
# __enter__, __exit__


class Session:
    def __init__(self, addr, port=8000):
        self.connected = False
        self.addr = addr
        self.port = port

    def __enter__(self):
        self.connected = True
        print(f'connected to {self.addr}:{self.port}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connected = False
        if exc_type is not None:
            print('Some error!')
        else:
            print('No problem')


localhost_session = Session('localhost')
with localhost_session as session:
    print(session is localhost_session)
    print(localhost_session.connected)

print(localhost_session.connected)


# інкапсуляція

class Secret:
    public_field = 'this is public'
    _private_field = 'avoid using this please'
    __real_secret = 'I am hidden'


s = Secret()
print(s.public_field)
print(s._private_field)
# print(s.__real_secret)
print(s._Secret__real_secret)


class PositiveNumber:
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value > 0:
            self.__value = new_value
        else:
            print('Only numbers greater zero accepted')


p = PositiveNumber
# p.value = 1
# print(p.value)
p.value = -1
print(p.value)
