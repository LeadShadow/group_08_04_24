"""
У цьому завданні ми:

Додамо поле для дня народження Birthday. Це поле не обов'язкове, але може бути тільки одне.
Додамо функціонал роботи з Birthday у клас Record, а саме функцію days_to_birthday,
яка повертає кількість днів до наступного дня народження.
Додамо функціонал перевірки на правильність наведених значень для полів Phone, Birthday.
Додамо пагінацію (посторінковий вивід) для AddressBook для ситуацій, коли книга дуже
велика і треба показати вміст частинами, а не все одразу. Реалізуємо це через створення
ітератора за записами.
Критерії прийому:
AddressBook реалізує метод iterator, який повертає генератор за записами AddressBook
і за одну ітерацію повертає уявлення для N записів.
Клас Record приймає ще один додатковий (опціональний) аргумент класу Birthday
Клас Record реалізує метод days_to_birthday, який повертає кількість днів до наступного
дня народження контакту, якщо день народження заданий.
setter та getter логіку для атрибутів value спадкоємців Field.
Перевірку на коректність веденого номера телефону setter для value класу Phone.
Перевірку на коректність веденого дня народження setter для value класу Birthday.

Optional:

Додати функціонал збереження адресної книги на диск та відновлення з диска. Для цього
ви можете вибрати будь-який зручний для вас протокол серіалізації/десеріалізації даних та
реалізувати методи, які дозволять зберегти всі дані у файл і завантажити їх із файлу.

Додати користувачеві можливість пошуку вмісту книги контактів, щоб можна було знайти всю
інформацію про одного або кількох користувачів за кількома цифрами номера телефону або літерами імені тощо.

Критерії прийому:
Програма не втрачає дані після виходу з програми та відновлює їх з файлу.
Програма виводить список користувачів, які мають в імені або номері телефону є збіги із введеним рядком.

from last lesson need improve:
start program with commands
added decorator - method __call__ in class InputError
"""

import re
from collections import UserDict
import datetime


N = 3


class Field:
    def __init__(self, value) -> None:
        self.value = value
        self.__value = None

    def __str__(self) -> str:
        return f'{self.value}'


class Name(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        def is_code_valid(phone_code: str) -> bool:
            if phone_code[:2] in ('03', '04', '05', '06', '09') and phone_code[2] != '0' and phone_code != '039':
                return True
            return False

        result = None
        phone = value.removeprefix('+').replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
        if phone.isdigit():
            if phone.startswith('0') and len(phone) == 10 and is_code_valid(phone[:3]):
                result = '+38' + phone
            if phone.startswith('380') and len(phone) == 12 and is_code_valid(phone[2:5]):
                result = '+' + phone
            if 10 <= len(phone) <= 14 and not phone.startswith('0') and not phone.startswith('380'):
                result = phone
        if result is None:
            raise ValueError(f'Неправильний тип значення: {value}')
        self.__value = result


class Birthday(Field):
    def __str__(self):
        if self.value is None:
            return 'Unknown'
        else:
            return f'{self.value:%d %b %Y}'

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        if value is None:
            self.__value = None
        else:
            try:
                self.__value = datetime.datetime.strptime(value, '%Y-%m-%d').date()
            except ValueError:
                try:
                    self.__value = datetime.datetime.strptime(value, '%d.%m.%Y').date()
                except ValueError:
                    raise DateIsNotValid


class Record:
    def __init__(self, name: Name, phones=None, birthday=None) -> None:
        if phones is None:
            phones = []
        self.name = name
        self.phone_list = phones
        self.birthday = birthday

    def __str__(self) -> str:
        return f'User {self.name} - Phones: {", ".join(self.phone_list)}, Birthday: {self.birthday}'

    def add_phone(self, phone: Phone) -> None:
        self.phone_list.append(phone.value)

    def del_phone(self, phone: Phone) -> None:
        self.phone_list.remove(phone.value)

    def edit_phone(self, phone: Phone, new_phone: Phone) -> None:
        self.phone_list.remove(phone.value)
        self.phone_list.append(new_phone.value)


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record


class PhoneUserAlreadyExists(Exception):
    """You cannot add existing phone number to a user"""


class DateIsNotValid(Exception):
    """You cannot add an invalid date"""


class InputError:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, contacts, *args):
        try:
            return self.func(contacts, *args)
        except IndexError:
            return 'Error! Give me name and phone or birthday please!'
        except KeyError:
            return 'Error! User not found!'
        except ValueError:
            return 'Error! Phone number is incorrect!'
        except PhoneUserAlreadyExists:
            return 'Error! You cannot add an existing phone number to s user'
        except DateIsNotValid:
            return 'Error! Date is not valid'


def verify_phone(phone):
    new_phone = re.sub(r'\+|\(|\)|-| | [a-zA-Zа-яА-Я]', '', phone)
    return new_phone


def salute(*args):
    return 'Hello! How can I help you?'


@InputError
def add_contact(contacts, *args):
    name = Name(args[0])
    phone = Phone(args[1])
    if name.value in contacts:
        if phone in contacts[name.value].phone_list:
            raise PhoneUserAlreadyExists
        else:
            contacts[name.value].add_phone(phone)  # contacts[name.value] -> record
            return f'Add phone {phone} to user {name}'
    else:
        if len(args) > 2:
            birthday = Birthday(args[2])
        else:
            birthday = Birthday(None)
        contacts[name.value] = Record(name, [phone.value], birthday)
        return f'Add user {name} with phone number {phone}, birthday: {birthday}'


@InputError
def change_contact(contacts, *args):
    name, old_phone, new_phone = args[0], args[1], args[2]
    new_phone = verify_phone(new_phone)
    old_phone = verify_phone(old_phone)
    contacts[name].edit_phone(Phone(old_phone), Phone(new_phone))
    return f'Change to user {name} phone number from {old_phone} to {new_phone}'


@InputError
def show_phone(contacts, *args):
    name = Name(args[0])
    phone = contacts[name.value]
    return f'{phone}'


@InputError
def add_birthday(contacts, *args):
    name, birthday = args[0], args[1]
    contacts[name].birthday = Birthday(birthday)
    return f'Add/modify birthday {contacts[name].birthday} to user {name}'


@InputError
def del_phone(contacts, *args):
    phone = verify_phone(args[1])
    name, phone = Name(args[0]), Phone(phone)
    contacts[name.value].del_phone(phone)
    return f'Delete phone {phone} from user {name}'


def show_all(contacts, *args):
    result = 'List of all users:'
    for key in contacts:
        result += f'\n{contacts[key]}'
    return result


def goodbye(*args):
    return 'Good bye!'


def unknown_command(*args):
    return 'Unknown command! Try again!'


def help_me(*args):
    return """Command format:
help or ? - help
hello - func of greeting
add <name> <phone> - add user to addressbook
change <name> <phone> - change the user's phone number
phone <name> - show the user's phone number
del <phone> - delete phone user
show all - show all contacts
birthday <name> <birthday> - add birthday to user <name>
close or . or exit or stop - exit the program"""


COMMANDS = {salute: ['hello'], add_contact: ['add '], change_contact: ['change '], help_me: ['?', 'help'],
            show_all: ['show all'], goodbye: ['good bye', 'close', 'exit', '.'], del_phone: ['del '],
            show_phone: ['phone '], add_birthday: ['birthday ']}


def command_parser(user_command: str) -> (str, list):
    for key, list_value in COMMANDS.items():
        for value in list_value:
            if user_command.lower().startswith(value):
                args = user_command[len(value):].split()
                return key, args
    else:
        return unknown_command, []


def main():
    contacts = AddressBook()
    print('Enter ? or help that find the command')
    while True:
        user_command = input('Enter command >>> ')
        command, data = command_parser(user_command)
        print(command(contacts, *data), '\n')
        if command is goodbye:
            break


if __name__ == "__main__":
    main()