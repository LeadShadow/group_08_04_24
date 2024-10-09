# Клас Stack
# Створіть клас Stack, що реалізує стек (структуру даних "остання прийшла — перша вийшла").
#
# Завдання:
#
# Реалізуйте методи для:
# Додавання елемента (push)
# Видалення елемента (pop)
# Виведення стека у вигляді рядка (__str__)

class PopFromEmptyStackError(Exception):
    def __str__(self):
        return 'Pop from empty stack'


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(-1)
        raise PopFromEmptyStackError

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
