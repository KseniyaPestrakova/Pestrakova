"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""
from _pytest.python_api import raises


# class Car:
#
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         if year > 2024:
#             raise Exception('Эта машина еще не была выпущена')
#         else:
#             self.year = year
#
#
#
# # код для проверки
# car = Car('Toyota', 'Corolla', 2022)
#
# car = Car('Toyota', 'Corolla', 3000)
# raises Exception('Эта машина еще не была выпущена')


"""
Напишите класс Person, представляющий человека, имеющий следующие атрибуты:

- имя
- возраст
- зарплата

Напишите класс Employee, у которого конструктор проверяет, что возраст не меньше 18 и не больше 127 лет.
В случае, если возраст не укладывается в заданные рамки, вызвать исключение ValueError и прервать выполнение программы.
Также в конструкторе необходимо проверять уровень зарплаты, который должен быть не меньше 16242. Вызывать ValueError
исключение.

Вызванные исключения должны пояснять в чем именно произошла ошибка.
"""


# class Person:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#
# class Employee(Person):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age, salary)
#         if age < 18 or age >= 127:
#             raise ValueError('Возраст должен быть не меньше 18 и не больше 127')
#         if salary < 16242:
#             raise ValueError('Оплата труда не может быть меньше 16242')
#
#
#
# # код для проверки
# # employee = Employee('John', 30, 5000)
# # raises ValueError('Оплата труда не может быть меньше 16242')
#
# # employee = Employee("Jane", 17, 50000)
# # raises ValueError('Возраст должен быть не меньше 18 и не больше 127')
#
# employee = Employee("Kate", 175, 50000)
# # raises ValueError('Возраст должен быть не меньше 18 и не больше 127')


"""
Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число
- Оценки - список из целых чисел, может быть пустым

Опишите класс Student и метод avg_rate так, чтобы считалась средняя оценка, а при пустом списке оценок возвращался 0

"""


class Student:

    def __init__(self, name, course, marks):

        self.name = name
        self.course = course
        self.marks = marks

    def avg_rate(self):
        if not self.marks:
            return 0

        else:
            avg_rate = sum(self.marks) / len(self.marks)
            return avg_rate





# код для проверки
student = Student('Ivan', 'Python', [5, 4, 5, 5])
print(student.avg_rate()) # 4.75

student = Student('Ivan', 'Python', [])
print(student.avg_rate()) # 0.0