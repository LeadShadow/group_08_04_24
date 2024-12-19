# У цій роботі ми продовжимо розвивати нашого віртуального асистента з CLI інтерфейсом.
#
# Наш асистент вже вміє взаємодіяти з користувачем за допомогою командного рядка,
# отримуючи команди та аргументи та виконуючи потрібні дії. У цьому завданні треба буде
# попрацювати над внутрішньою логікою асистента, над тим, як зберігаються дані, які саме дані
# і що з ними можна зробити.
#
# Застосуємо для цих цілей об'єктно-орієнтоване програмування. Спершу виділимо декілька
# сутностей (моделей) з якими працюватимемо.
#
# У користувача буде адресна книга або книга контактів. Ця книга контактів містить записи.
# Кожен запис містить деякий набір полів.
#
# Таким чином ми описали сутності (класи), які необхідно реалізувати. Далі розглянемо вимоги
# до цих класів та встановимо їх взаємозв'язок, правила, за якими вони будуть взаємодіяти.
#
# Користувач взаємодіє з книгой контактів, додаючи, видаляючи та редагуючи записи.
# Також користувач повинен мати можливість шукати в книзі контактів записи за одному
# або декількома критеріями (полям).
#
# Про поля також можна сказати, що вони можуть бути обов'язковими (ім'я) та необов'язковими
# (наприклад телефон або email). Також записи можуть містити декілька полів одного типу
# (наприклад декілька телефонів). Користувач повинен мати можливість
# додавати/видаляти/редагувати поля у будь-якому записі.
#
# Технічне завдання
# Розробіть систему класів для управління адресною книгою.
#
# Сутності:
#
# Field: Базовий клас для полів запису. Буде батьківським для всіх полів, у ньому реалізується логіка
# загальна для всіх полів
# Name: Клас для зберігання імені контакту. Обов'язкове поле.
# Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
# Необов'язкове поле з телефоном та таких один запис Record може містити декілька.
# Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
# Відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання
# обов'язкового поля Name
# AddressBook: Клас для зберігання та управління записами. Успадковується від UserDict,
# та містить логіку пошуку за записами до цього класу
# Функціональність:
#
# AddressBook:
# Додавання записів.
# Пошук записів за іменем.
# Видалення записів за іменем.
# Record:
# Додавання телефонів.
# Видалення телефонів.
# Редагування телефонів.
# Пошук телефону.
# Критерії приймання
# Клас AddressBook:
# Реалізовано метод add_record, який додає запис до self.data.
# Реалізовано метод find, який знаходить запис за ім'ям.
# Реалізовано метод delete, який видаляє запис за ім'ям.
# Записи Record у AddressBook зберігаються як значення у словнику. В якості ключів
# використовується значення Record.name.value.
# Клас Record:
# Реалізовано зберігання об'єкта Name в окремому атрибуті.
# Реалізовано зберігання списку об'єктів Phone в окремому атрибуті.
# Реалізовано методи для додавання - add_phone/видалення - remove_phone/редагування
# - edit_phone/пошуку об'єктів Phone - find_phone.
# Клас Phone:
# Реалізовано валідацію номера телефону (має бути 10 цифр).
# Реалізовано всі класи із завдання
import re
from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return f'{self.value}'


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phones=[]) -> None:
        self.name = name
        self.phone_list = phones

    def __str__(self) -> str:
        return f'User {self.name} - Phones: {", ".join(self.phone_list)}'

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


class InputError:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, contacts, *args):
        # try:
        return self.func(contacts, *args)
        # except Exception:
        #     print('dwada')


def verify_phone(phone):
    new_phone = re.sub(r'\+|\(|\)|-| | [a-zA-Zа-яА-Я]', '', phone)
    return new_phone


def salute(*args):
    return 'Hello! How can I help you?'


@InputError
def add_contact(contacts, *args):
    name = Name(args[0])
    phone = Phone(verify_phone(args[1]))
    if name.value in contacts:
        if phone in contacts[name.value].phone_list:
            raise PhoneUserAlreadyExists
        else:
            contacts[name.value].add_phone(phone)  # contacts[name.value] -> record
            return f'Add phone {phone} to user {name}'
    else:
        contacts[name.value] = Record(name, [phone.value])
        return f'Add user {name} with phone number {phone}'


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
show all - show all contacts
close or . or exit or stop - exit the program"""


if __name__ == "__main__":
    contacts = AddressBook()
    print(add_contact(contacts, 'Oleksandr', '+380937316048'))
    print(change_contact(contacts, 'Oleksandr', '+380937316048', '+380937316049'))
    print(show_phone(contacts, 'Oleksandr'))
    print(add_contact(contacts, 'Oleksandr', '+380937316050'))
    print(show_phone(contacts, 'Oleksandr'))
    print(del_phone(contacts, 'Oleksandr', '+380937316050'))
    print(show_phone(contacts, 'Oleksandr'))
    print(add_contact(contacts, 'Misha', '+380937316048'))
    print(show_all(contacts))