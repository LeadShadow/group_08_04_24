# Для попереднього завдання реалізуйте в класі Animal метод change_weight, який має
# змінювати вагу тварини.
#
# Викличте функцію change_weight(12) для об'єкта animal та змініть значення початкової
# ваги з 10 на 12 одиниць.


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


animal = Animal('Barsik', 10)
print(animal.weight)
# рік минув і Барсик набрав 2кг
animal.change_weight(12)
print(animal.weight)