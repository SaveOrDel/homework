# Все решения поместить в файл task03.py и разместить его на github

# Создать класс в конструктор которого передается одно число
# В этом классе дожен быть метод show, который распечатывает переданное число.
import random
import collections


class MyNum:
    """
    Контейнер для чисел
    """
    def __init__(self, value: int):
        self.data = value

    def show(self):
        print(self.data)


var1 = MyNum(7)
var1.show()


# Создать класс, который наследуется от предыдущего класса и в этот класс передается два числа.
# Данный класс реализует метод calc, который складывает эти два числа.
class MyNum2(MyNum):
    """
    Наследование и сложение
    """
    def __init__(self, value1: int, value2: int):
        super().__init__(value1)
        self.data2 = value2

    def calc(self):
        return self.data + self.data2


var2 = MyNum2(3, 4)
print(var2.calc())


# Создать блок try/except/finally
# Внутри блока try создать выражение, которое делит на 0.
# Перехватить эту ошибку и распечатать сообщение пользвоателю.
try:
    a = 7//0
except ZeroDivisionError:
    print("Ups, div by zero")
except Exception as e:
    print(f"Other error: {e}")
else:
    print("No Error")


# Создать декоратор, который перед запуском функции распечатывает все аргументы вызываемой функции.
def trace(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner


# Создать класс в котором применить декоартор  @property для доступа к внутренней переменной.
class MyNum3:
    def __init__(self):
        self._data = random.randint(1, 100)

    @property
    def data(self):
        return self._data


var3 = MyNum3()
print(var3.data)


# Создать генератор который возвращается числа от 1 до 10
def generator_1_10():
    i = 1
    while i <= 10:
        yield i
        i += 1


# С помощью стандартной функции collections.namedtuple создать объект для хранения точки в трехмерном пространстве.
Point = collections.namedtuple('Point', ['x', 'y', 'z'])
p1 = Point(1, 2, 3)

print(p1)

