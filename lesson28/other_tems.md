# Принцип інверсії залежностей (Dependency inversion)



Відповідно до принципу, класи повинні залежати від інших класів не напряму, а від абстракцій. Класи верхніх рівнів не повинні залежати від класів нижніх рівнів. Обидва типи класів повинні залежати від абстракцій. Абстракції не повинні залежати від деталей. Деталі повинні залежати від абстракцій. У процесі розробки програмного забезпечення існує момент, коли функціонал застосунку перестає поміщатися в межах одного модуля або класу. Коли це відбувається, нам доводиться вирішувати проблему залежностей класів (модулів). В результаті, наприклад, може виявитися так, що високорівневі компоненти залежать від низькорівневих компонентів.



```
import requests


class RequestConnection:
    def __init__(self, request):
        self.request = request

    def get_json_from_url(self, url):
        return self.request.get(url).json()


class ApiClient:
    def __init__(self, fetch: RequestConnection):
        self.fetch = fetch

    def get_data(self, url):
        response = self.fetch.get_json_from_url(url)
        return response


def data_adapter(data: dict):
    return [{f"{el.get('ccy')}": {"buy": float(el.get('buy')), "sale": float(el.get('sale'))}} for el in data]


def pretty_view(data):
    pattern = '|{:^10}|{:^10}|{:^10}|'
    print(pattern.format('currency', 'sale', 'buy'))
    for el in data:
        currency, *_ = el.keys()
        buy = el.get(currency).get('buy')
        sale = el.get(currency).get('sale')
        print(pattern.format(currency, sale, buy))


if __name__ == '__main__':
    api_client = ApiClient(RequestConnection(requests))
    
    data = api_client.get_data('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11')
    pretty_view(data_adapter(data))
```
# Принцип підстановки Барбари Лісков (Liskov substitution)



Принцип відкритості-закритості говорить про те, що у добре спроектованих програмах нова функціональність вводиться шляхом додавання нового коду, а не зміною старого, що вже працює. Принцип підстановки Лісков (далі LSP) — це як реалізувати цей принцип при побудові ієрархії наслідування класів в об'єктно-орієнтованих мовах програмування. По суті, правильна ієрархія наслідування в ООП - це ієрархія, побудована відповідно до LSP, щоб відповідати принципу відкритості-закритості.



У попередньому прикладі порушенням LSP була функція:


```
def total_area(shapes):
    sum = 0
    for el in shapes:
        if isinstance(el, Rect):
            sum += el.width * el.height
        if isinstance(el, Circle):
            sum += el.radius ** 2 * pi
    return sum
```


Тепер давайте розглянемо, як можна порушити LSP не таким очевидним способом. Припустимо, ми розробляємо програму, яка працює з геометричними фігурами. У ній є клас для роботи з прямокутниками:


```
class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area_of(self):
        return self.width * self.height
```


Тепер потрібно реалізувати фігуру квадрат. Квадрат – це очевидно прямокутник і цілком логічно, що клас Square повинен бути спадкоємцем класу Rect.


```
class Square(Rect):
    def __init__(self, size):
        Rect.__init__(self, size, size)

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height
```


І якщо у функції ми використовуємо клас Rect, а працюємо з конкретним класом Square, то можуть виникнути проблеми:


```
def test_shape_size(shape):
    shape.set_width(10)
    shape.set_height(20)
    return shape.area_of() == 200  # умова не спрацює, якщо shape — екземпляр класу Square
```


Відповідно до LSP нам необхідно використовувати спільний інтерфейс для обох класів і не наслідувати Square від Rect. Цей спільний інтерфейс повинен бути таким, щоб класи-спадкоємці могли б використовуватися замість батьківських класів, від яких вони утворені, не порушуючи роботу програми.


```
from enum import Enum


class SideType(Enum):
    TYPE_WIDTH = 'width'
    TYPE_HEIGHT = 'height'


class Shape:
    def set_side(self, size, side):
        pass

    def area_of(self):
        pass


class Rect(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_side(self, size, side):
        if SideType.TYPE_WIDTH == side:
            self.width = size
        if SideType.TYPE_HEIGHT == side:
            self.height = size

    def set_width(self, width):
        self.set_side(width, SideType.TYPE_WIDTH)

    def set_height(self, height):
        self.set_side(height, SideType.TYPE_HEIGHT)

    def area_of(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, size):
        self.edge = size

    def set_side(self, size, side=None):
        self.edge = size

    def set_width(self, width):
        self.set_side(width)

    def area_of(self):
        return self.edge ** 2


def get_area_of_shape(figure: Shape):
    return figure.area_of()

    
if __name__ == '__main__':
    square = Square(10)
    rect = Rect(5, 10)
    print('Square area: ', get_area_of_shape(square))
    print('Rect area: ', get_area_of_shape(rect))
```


Тепер поведінка спадкоємців не конфліктує із поведінкою базового класу. Це дозволить використовувати і Rect, і Square там, де оголошено використання Shape.