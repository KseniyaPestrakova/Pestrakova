"""
Создай класс Album у которого есть поля
- Исполнитель (artist) - строка
- Название (title) - строка
- Треки (tracks) - это **список**

**Создай два экземпляра album_1 и album_2**

Исполнитель: Queen
Название: Killer Queen
Треки: Brighton rock, Killer Queen, Tenement Funster

Исполнитель: Metallica
Название: Black Album
Треки: Enter Sandman, Sad But True, Holier Than Thou
"""


class Album:
    artist: str
    title: str
    tracks: list

    def __init__(self, artist, title, tracks):
        self.artist = artist
        self.title = title
        self.tracks = tracks


album_1 = Album('Queen', 'Killer Queen', ['Brighton rock', 'Killer Queen', 'Tenement Funster'])

album_2 = Album('Metallica', 'Black Album', ['Enter Sandman', 'Sad But True', 'Holier Than Thou'])


# код для проверки
print(album_1.artist, album_1.title, len(album_1.tracks), "треков")  # Queen Killer Queen 3 треков
print(album_2.artist, album_2.title, len(album_2.tracks), "треков")  # Metallica Black Album 3 треков
print(album_1)


"""
Создай класс Bottle (бутылка) c полями

- Цвет (color) - строка
- Объем (volume) - число с плавающей точкой

Создай три экземпляра

- Красную 0.7
- Белую 0.3
- Черную 1.0
"""


class Bottle:
    color: str
    volume: float

    def __init__(self, color, volume):
        self.color = color
        self.volume = volume


bottle_1 = Bottle("Красная", 0.7)
bottle_2 = Bottle("Белая", 0.3)
bottle_3 = Bottle("Черная", 1.0)


# код для проверки
print(bottle_1.color, bottle_1.volume)  # Красная 0.7
print(bottle_2.color, bottle_2.volume)  # Белая 0.3
print(bottle_3.color, bottle_3.volume)  # Черная 1.0


"""
Создай класс `Number` c полем `value` (указывается при инициализации)

Создай экземпляр, например `x = Number(7)`

Добавь методы:

`.get()` возвращает текущее value

`.add(<значение>)` добавляет указанное число к value

`.substract(<значение>)` вычитает указанное число из value
"""

class Number:
    value: float

    def __init__(self, value):
        self.value = value

    def get(self):
        print(self.value)

    def add(self, plus):
        self.value += plus

    def substract(self, minus):
        self.value -= minus



# код для проверки
n = Number(7)
print(n.get())  # 7
n.add(3)
print(n.get())  # 10
n.substract(5)
print(n.get())  # 5


"""
Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число

Создай два экземпляра

- Алиса , 3 [курс]
- Маргарита , 2 [курс]
"""


class Student:
    name: str
    course: int

    def __init__(self, name, course):
        self.name = name
        self.course = course
        ...


student_1 = Student('Алиса', 3)
student_2 = Student('Маргарита', 2)


# код для проверки
print(student_1.name, student_1.course)  # Алиса 3
print(student_2.name, student_2.course)  # Маргарита 2