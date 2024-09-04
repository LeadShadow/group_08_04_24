# Завдання 6: Форматування імен
# Опис завдання: У вас є список імен. Вам потрібно створити новий список, де кожне
# ім'я починається з великої літери.
# саша -> Саша

names = ['sasha', 'arsen', 'roma']

formatted_names = list(map(lambda name: name.title(), names))
print(formatted_names)

