"""
Напишите класс Animal, представляющий животное, имеющий следующие методы:
- __init__(self, name): конструктор, принимающий имя животного;
- speak(self): метод, который выводит звук, издаваемый животным.
Напишите класс Dog, наследующийся от класса Animal, представляющий собаку, имеющий следующие методы:
- speak(self): метод, который выводит звук, издаваемый собакой.
Напишите класс Cat, наследующийся от класса Animal, представляющий кошку, имеющий следующие методы:
- speak(self): метод, который выводит звук, издаваемый кошкой.
"""
import datetime

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print('Sound')
#
# class  Dog(Animal):
#     def speak(self):
#         print('woof')
#
# class Cat(Animal):
#     def speak(self):
#         print('meow')
#
#
#
# # код для проверки
# animal = Animal("Animal")
# animal.speak()  # ?
#
# dog = Dog("Dog")
# dog.speak()  # Woof!
#
# cat = Cat("Cat")
# cat.speak()  # Meow!


"""
Допишите код под условия в цикле так, чтобы вывод был корректным
"""

# class Animal:
#
#     def __init__(self, name):
#         self.name = name
#
#     def walk(self):
#         pass
#
#
# class Dog(Animal):
#
#     def bark(self):
#         print('Bark!')
#
#
# class Cat(Animal):
#
#     def meow(self):
#         print('Meow!')
#
#
#
# animals = [Dog('Dog1'), Dog('Dog2'), Cat('Cat1'), Dog('Dog3')]
#
# for animal in animals:
#     if isinstance(animal, Dog):
#         animal.bark()
#     else:
#         animal.meow()
# Должно выводиться Bark или Meow в зависимости от того какой класс

"""
Напишите класс Car, представляющий автомобиль, имеющий следующие методы:

- __init__(self, make, model, year): конструктор, принимающий марку автомобиля, модель и год выпуска;
- get_make(self): метод, который возвращает марку автомобиля;
- get_model(self): метод, который возвращает модель автомобиля;
- get_year(self): метод, который возвращает год выпуска автомобиля.

Напишите класс ElectricCar, наследующийся от класса Car, представляющий электромобиль, имеющий следующие методы:

- __init__(self, make, model, year, battery_size): конструктор, принимающий марку электромобиля, модель, год выпуска и размер батареи;
- get_battery_size(self): метод, который возвращает размер батареи электромобиля.
"""


# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def get_make(self):
#         return self.make
#
#     def get_model(self):
#         return self.model
#
#     def get_year(self):
#         return self.year
#
#
# class ElectricCar(Car):
#     def __init__(self, make, model, year, battery_size):
#         super().__init__(make, model, year)
#         self.battery_size = battery_size
#
#     def get_battery_size(self):
#         return self.battery_size
#
#
# # код для проверки
# car = Car("Tesla", "Model S", 2022)
# print(car.get_make())  # Tesla
# print(car.get_model())  # Model S
# print(car.get_year())  # 2022
#
# electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
# print(electric_car.get_make())  # Tesla
# print(electric_car.get_model())  # Model S
# print(electric_car.get_year())  # 2022
# print(electric_car.get_battery_size())  # 100


"""
Напишите класс Employee, представляющий сотрудника, имеющий следующие методы:

- __init__(self, name, salary): конструктор, принимающий имя сотрудника и его зарплату;
- get_salary(self): метод, который возвращает зарплату сотрудника.

Напишите класс Manager, наследующийся от класса Employee, представляющий менеджера, имеющий следующие методы:

- __init__(self, name, salary, bonus): конструктор, принимающий имя менеджера, его зарплату и бонус;
- get_salary(self): метод, который возвращает зарплату менеджера плюс его бонус.
"""


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def get_salary(self):
#         return self.salary
#
#
# class Manager(Employee):
#
#     def __init__(self, name, salary, bonus):
#         super().__init__(name, salary)
#         self.bonus =bonus
#
#     def get_salary(self):
#         return self.salary + self.bonus
#
#
#
# # код для проверки
# employee = Employee("John", 5000)
# print(employee.get_salary())  # 5000
#
# manager = Manager("Jane", 10000, 5000)
# print(manager.get_salary())  # 15000


"""
Для класса Employee и Client, опишите магический метод сложения таким образом, чтобы результатом сложения
было число, а прибавлять можно было только числа или другие объекты дочерних классов Employee

"""


# class Employee:
#
#     def __init__(self, pay):
#         self.pay = pay
#
#     def __add__(self, other):
#         return self.pay + other
#
#
#
# class Client:
#
#     def __init__(self, pay: int):
#         self.pay = pay
#
#
# class Developer(Employee):
#     pass
#
#
# class Manager(Employee):
#     pass
#
#
# # код для проверки
# users = [Employee(50000), Developer(50000), Manager(50000), Client(100000)]
#
# total_salary = 0
# for user in users:
#     if isinstance(user, (Employee, int)):
#         total_salary = user + total_salary
#
#
# print(total_salary)
# # Вывод: 150000

"""
Напишите класс Person, представляющий человека, имеющий следующие методы:

- __init__(self, name, age): конструктор, принимающий имя человека и его возраст;
- get_name(self): метод, который возвращает имя человека;
- get_age(self): метод, который возвращает возраст человека.

Напишите класс Student, наследующийся от класса Person, представляющий студента, имеющий следующие методы:

- __init__(self, name, age, major): конструктор, принимающий имя студента, его возраст и основной предмет
- get_major(self): метод, который возвращает основной предмет студента.
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
# class Student(Person):
#     def __init__(self, name, age, major):
#         super().__init__(name, age)
#         self.major = major
#
#     def get_major(self):
#         return self.major
#
#
# # код для проверки
# person = Person("Иван", 25)
# print(person.get_name())  # Иван
# print(person.get_age())  # 25
#
# student = Student("Мария", 20, "математика")
# print(student.get_name())  # Мария
# print(student.get_age())  # 20
# print(student.get_major())  # математика

"""
Напишите класс Shape, представляющий геометрическую фигуру, имеющий следующие методы:

- __init__(self, name): конструктор, принимающий имя геометрической фигуры;
- area(self): метод, который вычисляет площадь геометрической фигуры.

Напишите класс Rectangle, наследующийся от класса Shape, представляющий прямоугольник, имеющий следующие методы:

- __init__(self, name, width, height): конструктор, принимающий имя прямоугольника, ширину и высоту;
- area(self): метод, который вычисляет площадь прямоугольника.

Напишите класс Triangle, наследующийся от класса Shape, представляющий треугольник, имеющий следующие методы:

- __init__(self, name, base, height): конструктор, принимающий имя треугольника, основание и высоту;
- area(self): метод, который вычисляет площадь треугольника.
"""


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        print('площадь геометрической фигуры')

class Rectangle(Shape):

    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):

    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 1/2


# код для проверки
shape = Shape("Shape")
print(shape.area())  # 0

rect = Rectangle("Rectangle", 5, 10)
print(rect.area())  # 50

tri = Triangle("Triangle", 6, 4)
print(tri.area())  # 12
