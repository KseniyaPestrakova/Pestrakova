'''урок 11.2 Декораторы'''


def printing(function):
    def inner(*args, **kwargs):
        result = function(*args, **kwargs)
        print('result =', result)
        return result

    return inner


@printing
def add_one(x):
    return x + 1


y = add_one(10)
print(y)

'''Напишите декоратор, который проверяет, что все числа, возвращаемые декорируемой функцией,
 являются целыми, и округляет их до целых, если это не так.'''


def check_integers(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Проверка на тип с использованием type()
        if type(result) == float:
            return round(result)

        elif type(result) in (list, tuple):
            rounded = [round(x) if type(x) == float else x for x in result]
            # Возвращаем тот же тип, что и исходный (list или tuple)
            return type(result)(rounded)
        else:
            return result

    return wrapper


@check_integers
def checking_mub(x):
    return x


numbs = checking_mub([1, 2, 3.3, 10.0, 5.5765685])
print(numbs)

'''Напишите декоратор, который повторно вызывает декорируемую функцию три раза,
 каждый раз через три секунды, если произошла ошибка.'''

import time


def retry(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                return func(*args, **kwargs)
            except:
                time.sleep(3)
        raise Exception('Function call failed after multiple retries.')

    return wrapper


@retry
def func_time(x):
    return 10 / x


# check_time = func_time(0)
# print(check_time)


'''Напишите декоратор, который позволяет возвращать элементы декорируемой функции по одному через 
yield , если эта функция возвращает список или кортеж.'''


def yield_items(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Проверка на тип с использованием type()
        if type(result) in (list, tuple):
            for item in result:
                yield item
        else:
            yield result

    return wrapper


@yield_items
def func_items(*args):
    return args


check_items = func_items([1, 2, 3, 4], [5, 6])
print(list(check_items))

'''Напишите декоратор, который берет результат декорируемой функции (текст) и возвращает текст,
 в котором каждое слово сокращено до 8 символов. Если слово было сокращено, в конце слова ставится точка.'''


def shorten_words(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return " ".join(f"{word[:8]}." if len(word) > 8 else word for word in result.split())

    return wrapper


@shorten_words
def words_func(x: str):
    return x


check_words = words_func('Соответственно')
print(check_words)

'''Напишите три декоратора, которые можно применять последовательно к результату декорируемой функции.

Первый декоратор должен заменять в тексте, который выдает функция, все восклицательные знаки 
!  на !!!.
Второй декоратор должен заменять в тексте, который выдает функция, все знаки вопроса 
?  на ???.
Третий декоратор должен заменять в тексте, который выдает функция, все точки 
. на ... .'''


def exclamation_marks(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.replace("!", "!!!")

    return wrapper


def question_marks(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.replace("?", "???")

    return wrapper


def dots(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.replace(".", "...")

    return wrapper


@exclamation_marks
@question_marks
@dots
def my_function():
    return "Что? Где! Когда."


print(my_function())

'''Напишите декоратор, который проверяет, что все числа, возвращаемые декорируемой функцией,
 являются целыми, и округляет их до целых, если это не так. Декоратор должен принимать параметр 
precision, который указывает, до скольких цифр после запятой округлять числа.'''

from functools import wraps


def check_floats(precision):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            # Проверка на тип с использованием type()
            if type(result) == float:
                return round(result, precision)
            elif type(result) in (list, tuple):
                rounded = [round(x, precision) if type(x) == float else x for x in result]
                return type(result)(rounded)
            else:
                return result

        return inner

    return decorator


'''Напишите декоратор, который повторно вызывает декорируемую функцию заданное количество раз через заданное время,
 если произошла ошибка. Параметры, передаваемые в декоратор, обязательно должны быть именованными.'''

from functools import wraps
import time


def retry(*, retries=3, delay=3):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except:
                    time.sleep(delay)
            raise Exception('Function call failed after multiple retries.')

        return inner

    return wrapper


'''Напишите декоратор, который берет результат декорируемой функции (текст) и возвращает текст,
 в котором каждое слово сокращено до определенной длины. Если слово было сокращено, в конце слова
  ставится переданный символ. Количество символов в слове и знак в конце сокращенного слова — параметры
   декоратора, причем символ обязательно должен передаваться как именованный аргумент.'''


from functools import wraps

def shorten_words(max_len, *, end_symbol='.'):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return " ".join(f"{word[:max_len]}{end_symbol}" if len(word) > max_len else word for word in result.split())
        return inner
    return wrapper


@shorten_words(3, end_symbol='!')
def some_func():
    return "Красный Белый Синий."

print(some_func())


'''Напишите тесты с использованием библиотеки pytest для проверки корректности работы декоратора из предыдущей задачи.'''

import pytest

# Тестируемая функция
@shorten_words(4, end_symbol='!')
def get_text():
    return "Красный Белый Синий."

# Тесты
# def test_shortening():
#     assert get_text() == "Крас! Белы! Сини!"
#
# def test_no_shortening():
#     @shorten_words(10, end_symbol='!')
#     def get_long_text():
#         return "Красный Белый Синий."
#     assert get_long_text() == "Красный Белый Синий."
#
# def test_end_symbol():
#     @shorten_words(3, end_symbol='?')
#     def get_questioned_text():
#         return "Красный Белый Синий."
#     assert get_questioned_text() == "Кра? Бел? Син?"
#
# def test_different_lengths():
#     @shorten_words(5, end_symbol='.')
#     def get_different_length_text():
#         return "Hello beautiful world"
#     assert get_different_length_text() == "Hello beaut. world"



'''Создайте декоратор @positive_integers, который проверяет, что все аргументы функции — положительные целые числа. Если аргумент — неположительное число,
 выбрасывается исключение ValueError с сообщением All arguments must be positive integers.
 
Пример использования:

@positive_integers
def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

multiply(2, 3, 4) # Вывод: 24
multiply(2, 0, 4) # Выбрасывает исключение ValueError с сообщением "All arguments must be positive integers'''


def positive_integers(func):
    def wrapper(*args):
        for arg in args:
            if arg <= 0:
                raise ValueError('All arguments must be positive integers')
        return func(*args)
    return wrapper


@positive_integers
def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

print(multiply(2, 3, 4))
# print(multiply(2, 0, 4))


'''Создайте декоратор @is_palindrome, который проверяет, что аргумент функции является палиндромом (строкой,
 которая читается одинаково слева направо и справа налево). Если аргумент не является палиндромом, выбрасывается
  исключение ValueError с сообщением Argument must be a palindrome.
Пример использования:

@is_palindrome
def reverse_string(string):
    return string[::-1]

reverse_string('racecar') # "racecar"
reverse_string('Racecar') # "racecaR"
reverse_string('hello') # Выбрасывает исключение ValueError с сообщением "Argument must be a palindrome"'''


def is_palindrome(func):
    def wrapper(text):
        if text.lower() != text[::-1].lower():
            raise ValueError('Argument must be a palindrome')
        return func(text)
    return wrapper

@is_palindrome
def reverse_string(string):
    return string[::-1]

print(reverse_string('racecar'))
print(reverse_string('Racecar'))
# reverse_string('hello')


'''Создайте декоратор @logging, который будет логировать вызовы функции и ее результат. Лог должен выводиться на экран.
Пример вывода:
@logging
def multiply(x, y):
    return x * y
multiply(2, 3) 
>>> Function multiply called with args: (2, 3) and kwargs: {}. Result: 6'''


def logging(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Function {func.__name__} called with args: {args} and kwargs: {kwargs}. Result: {result}')
        return result
    return wrapper

@logging
def multiply(x, y):
    return x * y
multiply(2, 3)


'''Создайте декоратор @memoize, который кеширует результаты функции для определенных аргументов.
Если функция вызывается с теми же аргументами, что и в предыдущий раз, она должна возвращать результат
из кеша, а не вычислять его заново. Также создайте два дополнительных декоратора:
@slowit(n)
 — декоратор с параметрами, которые замедляют работу функции на n секунд. Без параметров декоратор замедляет
  функцию на 1 секунду. В декораторе используется функция time.sleep(n).
@timeit
 — декоратор, который выводит время работы функции.'''

from functools import reduce
from time import sleep, time


def slowit(n=1):
    def decorator(func):
        def wrapper(*args):
            sleep(n)
            return func(*args)
        return wrapper
    return decorator


def timeit(func):
    def wrapper(*args):
        start_time = time()
        result =  func(*args)
        end_time = time()
        print(f'Time: {end_time - start_time:.6f}')
        return result
    return wrapper


def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return  cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper



@timeit
@slowit(2)
def product(n):
    return reduce(lambda x, y: x * y, range(1, n+1)) if n > 0 else None

product(10)
product(10)

# С кешированием время работы функции при первом вызове не менее 2 секунд, при втором вызове почти мгновенно.
@timeit
@memoize
@slowit(2)
def product(n):
    return reduce(lambda x, y: x * y, range(1, n+1)) if n > 0 else None

product(10)
product(10)