"""
Напишите класс Bird, представляющий птицу, имеющий следующие методы:
- fly(self): метод, который выводит сообщение "Flying".
Напишите класс Penguin, наследующийся от класса Bird, представляющий пингвина, имеющий следующие методы:
- fly(self): метод, который выводит сообщение "I am a penguin and cannot fly".
Напишите класс Eagle, наследующийся от класса Bird, представляющий орла, имеющий следующие методы:
- hunt(self): метод, который выводит сообщение "Hunting".
"""

# class Bird:
#     def fly(self):
#         print("Flying")
#
#
# class Penguin(Bird):
#     def fly(self):
#         print("I am a penguin and cannot fly")
#
#
# class Eagle(Bird):
#     def hunt(self):
#         print("Hunting")
#
#
# # код для проверки
# bird = Bird()
# bird.fly()  # Flying
#
# penguin = Penguin()
# penguin.fly()  # I am a penguin and cannot fly
#
# eagle = Eagle()
# eagle.fly()  # Flying
# eagle.hunt()  # Hunting


"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Так как данный класс используется в большом каталоге, его необходимо оптимизировать и создать класс, который использует
коллекции slots

Сравните скорость работы двух классов: с коллекциями slots и без них. Для этого каждому классу напишите метод 
get_set_del, в котором происходи получение, присваивание и удаление значения.
"""


# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def get_set_del(self):
#         self.brand = 'new brand'
#         del self.brand
#
#
# class CarSlots:
#     __slots__ = ('brand', 'model', 'year')
#
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def get_set_del(self):
#         self.brand = 'new brand'
#         del self.brand
#
#
# car = Car('Toyota', 'Corolla', 2022)
# car_slots = CarSlots('Toyota', 'Crown', 1990)
#
# import timeit
#
# t1 = timeit.timeit(car.get_set_del)
# t2 = timeit.timeit(car_slots.get_set_del)
# print((t1 - t2) / t1 * 100)


"""
Напишите класс Person, представляющий человека, имеющий следующие методы:

- __init__(self, name, age): конструктор, принимающий имя человека и его возраст;
- get_name(self): метод, который возвращает имя человека;
- get_age(self): метод, который возвращает возраст человека.

Напишите класс Employee2, наследующийся от класса Person, представляющий сотрудника, имеющий следующие методы:

- __init__(self, name, age, salary): конструктор, принимающий имя сотрудника, его возраст и зарплату;
- get_salary(self): метод, который возвращает зарплату сотрудника.

Напишите класс Manager2, наследующийся от класса Employee2, представляющий менеджера, имеющий следующие методы:

- __init__(self, name, age, salary, bonus): конструктор, принимающий имя менеджера, его возраст, зарплату и бонус;
- get_bonus(self): метод, который возвращает бонус менеджера.
"""


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#
# class Employee2(Person):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.salary = salary
#
#     def get_salary(self):
#         return self.salary
#
# class Manager2(Employee2):
#     def __init__(self, name, age, salary, bonus):
#         super().__init__(name, age, salary)
#         self.bonus = bonus
#
#     def get_bonus(self):
#         return self.bonus
#
#
#
#
# # код для проверки
# person = Person("John", 30)
# print(person.get_name())  # John
# print(person.get_age())  # 30
#
# employee = Employee2("Jane", 25, 5000)
# print(employee.get_name())  # Jane
# print(employee.get_age())  # 25
# print(employee.get_salary())  # 5000
#
# manager = Manager2("Bob", 40, 10000, 5000)
# print(manager.get_name())  # Bob
# print(manager.get_age())  # 40
# print(manager.get_salary())  # 10000
# print(manager.get_bonus())  # 5000

"""
Напишите класс Student, представляющий студента, имеющий следующие атрибуты:

- __slots__ = ('name', 'age', 'grades'): список атрибутов, доступных объекту.

Напишите класс Course, представляющий курс, имеющий следующие атрибуты:

- __slots__ = ('name', 'students'): список атрибутов, доступных объекту.
"""


class Student:
    __slots__ = ('name', 'age', 'grades')

class Course:
    __slots__ = ('name', 'students')


# код для проверки
student1 = Student()
student1.name = "John"
student1.age = 20
student1.grades = [90, 80, 85]

student2 = Student()
student2.name = "Jane"
student2.age = 21
student2.grades = [95, 85, 90]

course = Course()
course.name = "Math"
course.students = [student1, student2]
