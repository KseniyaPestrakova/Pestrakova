"""
Напишите класс BankAccount, имеющий следующие свойства и методы:

- __init__(self, balance): конструктор, принимающий начальный баланс счета
- balance: свойство, которое возвращает текущий баланс счета
- deposit(self, amount): метод, который позволяет внести деньги на счет
- withdraw(self, amount): метод, который позволяет снять деньги со счета
- close(self): метод, который закрывает счет и возвращает оставшиеся на нем деньги

Для свойства balance используйте декоратор @property.
"""


# class BankAccount:
#     balance: int
#
#     def __init__(self, balance):
#         self.balance = balance
#
#     @property
#     def balance(self):
#         '''возвращает текущий баланс'''
#         return self._balance
#
#     @balance.setter
#     def balance(self, balance):
#         self._balance = balance
#
#     def deposit(self, amount: int):
#         self.balance += amount
#
#     def withdraw(self, amount: int):
#         self.balance -= amount
#
#     def close(self):
#         self.balance -= self.balance
#
#
# if __name__ == '__main__':
#     # код для проверки
#     account = BankAccount(1000)
#     print(account.balance)  # 1000
#
#     account.deposit(500)
#     print(account.balance)  # 1500
#
#     account.withdraw(200)
#     print(account.balance)  # 1300
#
#     account.close()
#     print(account.balance)  # 0

"""
Напишите класс Person, имеющий следующие методы:

- __init__(self, name, age): конструктор, принимающий имя и возраст человека
- display(self): метод, выводящий на экран имя и возраст человека
- from_birth_year(cls, name, birth_year): класс-метод, принимающий имя и год рождения человека и
возвращающий объект класса Person;
- is_adult(cls, age): статический метод, принимающий возраст человека и возвращающий True,
если он старше 18 лет, и False в противном случае
"""

# from datetime import datetime
#
#
# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     def display(self):
#         return f'{self.name}, {self.age} лет'
#
#     @classmethod
#     def from_birth_year(cls, name, birth_year):
#         cls.name = name
#         age = datetime.now().year - birth_year
#         return cls(name, age)
#
#     @staticmethod
#     def is_adult(age: int):
#         if age >= 18:
#             return True
#         return False
#
#
#
#
#
# # код для проверки
# person1 = Person("John", 28)
# print(person1.display())  # John is 28 years old
#
#
# person2 = Person.from_birth_year("Mike", 1995)
#
# print(person2.display())  # Mike is 26 years old
#
# print(Person.is_adult(20))  # True
# print(Person.is_adult(15))  # False

"""
Напишите класс Rectangle, имеющий следующие методы:

- __init__(self, width, height): конструктор, принимающий ширину и высоту прямоугольника
- area(self): метод, возвращающий площадь прямоугольника
- perimeter(self): метод, возвращающий периметр прямоугольника
- from_diagonal(cls, diagonal, aspect_ratio): класс-метод, принимающий диагональ прямоугольника и соотношение сторон и возвращающий объект класса Rectangle
- is_square(width, height): статический метод, принимающий ширину и высоту прямоугольника и возвращающий True,
если это квадрат, и False в противном случае
"""

# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return (self.width + self.height) * 2
#
#     @classmethod
#     def from_diagonal(cls, diagonal, aspect_ratio):
#         width = diagonal / (1 + aspect_ratio ** 2) ** 0.5
#         height = width / aspect_ratio
#
#         return cls(width, height)
#
#     @staticmethod
#     def is_square(width, height):
#         if width == height:
#             return True
#         return False


# код для проверки
# rectangle = Rectangle(4, 5)
# print(rectangle.area())  # 20
# print(rectangle.perimeter())  # 18
#
# rectangle2 = Rectangle.from_diagonal(5, 2)
# print(rectangle2.area())  # 10.0128
# print(rectangle2.perimeter())  # 13.42
#
# print(Rectangle.is_square(4, 4))  # True
# print(Rectangle.is_square(4, 5))  # False


"""
Напишите класс User, имеющий следующие свойства и методы:

- __init__(self, name, password): конструктор, принимающий имя пользователя и пароль
- name: свойство, которое возвращает имя пользователя
- password: свойство, которое позволяет установить или изменить пароль пользователя
- is_admin: свойство, которое возвращает, является ли пользователь администратором или нет
- _is_admin: свойство-помощник, которое определяет, является ли пользователь администратором или нет
- login(self, password): метод, который проверяет, соответствует ли введенный пароль паролю пользователя
- logout(self): метод, который выходит из аккаунта пользователя (устанавливает значение свойства _is_logged_in в False при условии, что пользователь залогинен)

Для свойств name и password используйте декораторы @property и @password.setter.
"""


class User:
    name: str
    password: str

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self._is_logged_in = False
        self._is_admin = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @property
    def is_admin(self):
        return self._is_admin

    @is_admin.setter
    def is_admin(self, _is_admin):
        self._is_admin = False

    def _is_admin(self, _is_admin):
        self._is_admin = True

    def login(self, password):

        if password == self._password:
            self._is_logged_in = True
            return True
        return False

    def logout(self):
        if self._is_logged_in:
            self._is_logged_in = False
            print("Выход из аккаунта выполнен.")


# код для проверки
user1 = User("Alice", "qwerty")
print(user1.name)  # Alice
print(user1.password)  # qwerty
print(user1.is_admin)  # False

user1.password = "newpassword"
print(user1.password)  # newpassword

user1._is_admin = True
print(user1.is_admin)  # True
#
user1.login("newpassword")  # True
user1.logout()