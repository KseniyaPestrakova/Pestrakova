"""
Напишите класс Counter, имеющий следующие методы:

- __init__(self): конструктор, создающий счетчик и устанавливающий его значение в 0;
- __call__(self): магический метод, который позволяет использовать объект класса Counter как функцию, возвращающую текущее значение счетчика;
- increment(self): метод, увеличивающий значение счетчика на 1.
"""

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self):
#         return self.__counter
#
#     def increment(self):
#         self.__counter += 1
#
#
# # код для проверки
# counter = Counter()
# print(counter())  # 0
#
# counter.increment()
# print(counter())  # 1
#
# counter.increment()
# print(counter())  # 2


"""
Напишите класс Fraction, представляющий собой дробь, имеющий следующие методы:

- __init__(self, numerator, denominator): конструктор, принимающий числитель и знаменатель дроби;
- __repr__(self): магический метод, возвращающий строковое представление дроби,
которое можно использовать для создания нового объекта класса Fraction;
- __str__(self): магический метод, возвращающий строковое представление дроби;
- __add__(self, other): магический метод, который позволяет складывать дроби и возвращать новую дробь.
"""

# def gcd(numerator, denominator):
#     while denominator:
#         numerator, denominator = denominator, numerator % denominator
#     return numerator
#
# class Fraction:
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator
#         self.gcd = self.denominator, self.numerator % self.denominator
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}({self.numerator}, {self.denominator})"
#
#     def __str__(self):
#         return f'{self.numerator}/{self.denominator}'
#
#
#
#     def __add__(self, other):
#         common_gcd = gcd(other.denominator, self.denominator)
#         new_numerator = (self.numerator * other.denominator + other.numerator * self.denominator) // common_gcd
#         new_denominator = (self.denominator * other.denominator) // common_gcd
#         return f'{new_numerator}/{new_denominator}'
#
#
# # код для проверки
# fraction1 = Fraction(1, 2)
# print(repr(fraction1))  # Fraction(1, 2)
# print(str(fraction1))  # 1/2
#
# fraction2 = Fraction(3, 4)
# fraction3 = fraction1 + fraction2
# print(fraction3)  # 5/4


"""
Напишите класс Logger, имеющий следующие методы:

- __init__(self, filename): конструктор, принимающий имя файла, в который будет производиться запись логов;
- __call__(self, message): магический метод, который позволяет использовать объект класса Logger как функцию,
принимающую сообщение и записывающую его в файл.
"""

# class Logger:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def __call__(self, message):
#         with open(self.filename, 'w') as f:
#             f.write(message)
#
#
# # код для проверки
# logger = Logger("log.txt")
# logger("This is a test message.")


# """
# Напишите класс MyList, представляющий собой список, имеющий следующие методы:
#
# - __init__(self, data): конструктор, принимающий список элементов;
# - __repr__(self): магический метод, возвращающий строковое представление списка,
# которое можно использовать для создания нового объекта класса MyList;
# - __str__(self): магический метод, возвращающий строковое представление списка;
# - __len__(self): магический метод, возвращающий длину списка;
# - __add__(self, other): магический метод, который позволяет складывать списки и возвращать новый список.
# """
#
#
# class MyList:
#     def __init__(self, data):
#         self.data = data
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}({self.data})"
#
#     def __str__(self):
#         return f"{self.data})"
#
#     def __len__(self):
#         return len(self.data)
#
#     def __add__(self, other):
#         return  self.data + other.data
#
#
#
# # код для проверки
# my_list1 = MyList([1, 2, 3])
# print(repr(my_list1))  # MyList([1, 2, 3])
# print(str(my_list1))  # [1, 2, 3]
# print(len(my_list1))  # 3
#
# my_list2 = MyList([4, 5, 6])
# my_list3 = my_list1 + my_list2
# print(my_list3)  # [1, 2, 3, 4, 5, 6]

# """
# Напишите класс MyList2, который будет работать аналогично встроенному классу list(). Класс должен иметь следующие методы:
#
# - __init__(self, data): конструктор, принимающий список элементов;
# - __iter__(self): магический метод, который возвращает итератор;
# - __next__(self): магический метод, который возвращает следующий элемент последовательности;
# - __getitem__(self, index): магический метод, который позволяет обратиться к элементу списка по индексу.
# """
#
#
# class MyList2:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         self.index = 0
#         return self
#
#     def __next__(self):
#         if self.index < len(self.data):
#             result = self.data[self.index]
#             self.index += 1
#             return result
#         else:
#             raise StopIteration
#
#     def __getitem__(self, index):
#         if index < len(self.data):
#             return self.data[index]
#         else:
#             raise IndexError("Index out of range")
#
#
# # код для проверки
# my_list = MyList2([1, 2, 3])
# for i in my_list:
#     print(i)  # 1 2 3
#
# print(my_list[1])  # 2

# """
# Напишите класс Point, представляющий собой точку на плоскости, имеющий следующие методы:
#
# - __init__(self, x, y): конструктор, принимающий координаты точки;
# - __repr__(self): магический метод, возвращающий строковое представление точки, которое можно использовать для создания нового объекта класса Point;
# - __str__(self): магический метод, возвращающий строковое представление точки;
# - __add__(self, other): магический метод, который позволяет складывать точки и возвращать новую точку.
# """
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}({self.x}, {self.y})"
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#
#
# # код для проверки
# point1 = Point(1, 2)
# print(repr(point1))  # Point(1, 2)
# print(str(point1))  # (1, 2)
#
# point2 = Point(3, 4)
# point3 = point1 + point2
# print(point3)  # (4, 6)


"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""


import time
class Timer:

    def __init__(self):
        self.elapsed_time = time.time()

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.elapsed_time = self.end - self.start



with Timer() as timer:
    time.sleep(1)

    # код для проверки
    print("Execution time:", timer.elapsed_time)
