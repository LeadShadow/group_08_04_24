# Підрахунок суми чисел у списку:
# Напишіть програму, яка приймає список чисел і обчислює їхню суму.
numbers = [1, 2, 3, 4, 5]  # 1 + 2 + 3 + 4 + 5
sum_ = 0
for num in numbers:
    sum_ += num

print(f'sum of numbers in list: {sum_}')
