# Клас FileWriter
# Створіть клас FileWriter, який дозволяє записувати дані у файл.
#
# Завдання:
#
# Реалізуйте метод __enter__, щоб відкривати файл у режимі запису.
# Реалізуйте метод __exit__, щоб закривати файл після використання.
# Реалізуйте метод write, щоб записувати рядки у файл.


class FileWriter:
    def __init__(self, filename, regime):
        self.filename = filename
        self.regime = regime

    def __enter__(self):
        self.file = open(self.filename, self.regime)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def write(self, data):
        self.file.write(data + '\n')


with FileWriter('output.txt', 'w') as writer:
    writer.write('Hello world!')
    writer.write('This is a test task')


with open('output1.txt', 'w') as writer:
    writer.write('Hello world!2' + '\n')
    writer.write('This is a test task.2' + '\n')

