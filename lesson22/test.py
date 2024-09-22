# Контейнери створені за допомогою наслідування UserList, UserDict, UserString
from collections import UserDict, UserList, UserString
import string

# UserDict(всередині має поле self.data = {})


class ValueSearchableDict(UserDict):
    def has_in_value(self, value):
        return value in self.data.values()


class A:
    def say_hello(self):
        print('Hello!')


as_dict = ValueSearchableDict()
as_dict['a'] = 1
print(as_dict.has_in_value(1))
print(as_dict)

a = A()
print(a)


class ValueSearchableDict:
    def __init__(self):
        self.data = {}

    def has_in_value(self, value):
        return value in self.data.values()


v = ValueSearchableDict()
print(v)


class CountableList(UserList):
    def sum_(self):
        return sum(self.data)


countable = CountableList([1, 2, 3, 4, 5])
print(countable)
print(countable.sum_())


class TruncatedString(UserString):
    MAX_LEN = 7

    def truncate(self):
        self.data = self.data[:self.MAX_LEN]


ts = TruncatedString('hello world')
ts.truncate()
print(ts)
print(ts.data)


# власні винятки
class NameTooShortError(Exception):
    pass


class NameStartsFromLowError(Exception):
    def __str__(self):
        return "Ім'я починається з маленької літери"


def enter_name():
    name = input('Enter name: ')
    if len(name) < 3:
        raise NameTooShortError
    if name[0] in string.ascii_lowercase:  # 'O'
        raise NameStartsFromLowError()
    print("Успішне введення імені")


enter_name()
# магічні методи
print(NameStartsFromLowError())
print(A())