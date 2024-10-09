# 1. Клас Counter
# Створіть клас Counter, який рахує, скільки разів було викликано метод increment.
#
# Завдання:
#
# Реалізуйте метод increment, який збільшує лічильник на 1.
# Реалізуйте метод __str__, щоб виводити значення лічильника.

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def __str__(self):
        return f'Current count: {self.count}'


counter = Counter()
# перше підключення до бд
counter.increment()
# друге підключення до бд
counter.increment()
print(counter)
