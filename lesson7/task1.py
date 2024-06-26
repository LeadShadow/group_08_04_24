# При аналізі даних часто виникає необхідність позбавитися екстремальних значень,
# перш ніж почати працювати з даними далі. Напишіть функцію prepare_data, яка видаляє
# з переданого списку найбільше та найменше значення, сортує його в порядку зростання і
# повертає змінений список як результат.

def prepare_data(list1):  # [1, 10, 4, 7, 1231231, -2, -5, -10, 55]
    list1.sort()
    list1.pop(0)
    list1.pop(-1)
    return list1


print(prepare_data([1, 10, 4, 7, 1231231, -2, -5, -10, 55]))