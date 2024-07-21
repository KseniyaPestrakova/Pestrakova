'''Вам дан текст сообщения:

text = \'''Visit my website at https://www.example.com
or you can check out https://www.someotherexample.com\'''
Напишите и примените регулярное выражение, чтобы получить список всех URL-адресов.'''
import re

# import re
#
# text = '''
# Visit my website at https://www.example.com
# or you can check out https://www.someotherexample.com
# '''
#
# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
#
# matches = pattern.finditer(text)
#
# urls = [match.group() for match in matches]
#
# print(urls)


'''У вас есть текст сообщения:

text = 'Позвоните мне по номеру 555-123-4567 или 555-987-6543'
Напишите и примените регулярное выражение, чтобы извлечь номера телефонов, т. е. найти любую последовательность из
10 цифр, которая может представлять собой номер телефона.'''

# import re
#
# text = 'Позвоните мне по номеру 555-123-4567 или 555-987-6543'
#
#
# pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
#
# matches = pattern.findall(text)
#
# print(matches)


'''Вам дана строка:

text = 'Цвет неба - синий.'
Напишите и примените регулярное выражение, чтобы заменить все вхождения слова синий на слово blue.'''

# import re
#
# text = 'Цвет неба - синий.'
#
# change_text = re.sub('синий', 'blue', text)
# print(change_text)


'''Дан файл 
access.log
, содержащий большой объем текста и email-адресов. Необходимо с помощью регулярных выражений «вытащить» оттуда все email-адреса, подсчитать количество вхождений каждого домена почтового сервиса и сохранить результат в JSON-файле 
result.json
.

Для решения задачи необходимо использовать библиотеки re, json и collections.

Содержание файла 
access.log:

[2021-10-20 10:23:45] INFO: User john.doe@gmail.com logged in
[2021-10-20 10:23:46] INFO: User alice.smith@yahoo.com logged in
[2021-10-20 10:23:47] INFO: User bob.johnson@gmail.com logged in
[2021-10-20 10:23:48] DEBUG: Loading user data for sarah.jones@gmail.com
[2021-10-20 10:23:49] DEBUG: User sarah.jones@gmail.com has been granted admin privileges
[2021-10-20 10:23:50] WARNING: User mike.peters@hotmail.com has not confirmed their email address
[2021-10-20 10:23:51] ERROR: Failed to send email to jane.doe@gmail.com
[2021-10-20 10:23:51] ERROR: Error message: Connection timed out
[2021-10-20 10:23:52] DEBUG: User sam.wilson@yahoo.com has updated their profile information
[2021-10-20 10:23:53] INFO: User mark.thompson@gmail.com logged in
[2021-10-20 10:23:54] DEBUG: Loading user data for kelly.brown@gmail.com
[2021-10-20 10:23:55] DEBUG: User kelly.brown@gmail.com has been granted read-only access
[2021-10-20 10:23:56] ERROR: Traceback (most recent call last):
  File "/path/to/my/script.py", line 42, in ‹module›
    my_function()
  File "/path/to/my/script.py", line 23, in my_function
    result = my_other_function()
  File "/path/to/my/other/script.py", line 12, in my_other_function
    raise ValueError("Invalid input")
ValueError: Invalid input
Пример текста для теста:

Это пример текста, в котором есть email-адреса: example@gmail.com, mail@example.com, test@mail.ru, user@yandex.ru.
Также в тексте могут быть другие email-адреса, например, admin@domain.com.'''

# import re
# import json
# from collections import Counter
#
# def count_emails(input_file: str, output_file: str):
#     # Открываем файл с текстом и считываем его содержимое
#     with open(input_file, "r", encoding="utf-8") as f:
#         text = f.read()
#
#     # Находим все email-адреса в тексте с помощью регулярного выражения
#     pattern = r"\b[\w\.-]+@[\w\.-]+\.\w+\b"
#     email_addresses = re.findall(pattern, text)
#
#     # Создаем объект Counter, хранящий количество email-адресов каждого почтового сервиса
#     email_counts = Counter(email.split('@')[1] for email in email_addresses)
#
#     # Создаем словарь, хранящий метаинформацию и списки email-адресов для каждого домена
#     result = {"total_count": len(email_addresses), "domains": {}}
#     for domain, count in email_counts.items():
#         # Получаем список email-адресов для данного домена
#         domain_emails = [email for email in email_addresses if email.split('@')[1] == domain]
#         # Добавляем информацию о домене в словарь
#         result["domains"][domain] = {"count": count, "emails": domain_emails}
#
#     # Записываем результат в JSON-файл
#     with open(output_file, "w", encoding="utf-8") as f:
#         json.dump(result, f, ensure_ascii=False, indent=4)
#
# if __name__ == '__main__':
#     count_emails("..\\logs\\access.log", "result.json")


'''Напишите программу, которая находит все даты в формате "dd-mm-yyyy" в заданном тексте.'''

# import re
#
# text = 'Сегодня 23-09-2024, а завтра будет 24-09-2024. Вчера было 22-09-2024'
#
# pattern = r'\b\d{2}[-]\d{2}[-]\d{4}\b'
#
# dates = re.findall(pattern, text)
# print(dates)

'''Напишите программу, которая извлекает все хештеги из заданного текста.'''

# import re
#
# text = 'Сегодня #Python, а завтра будет #MachineLearning. Вчера было #DataDcience.'
#
# pattern = r'#\w+'
# hash_list = re.findall(pattern, text)
#
# print(hash_list)

'''Напишите программу, которая проверяет строки на соответствие требованиям пароля: длина не менее 8 символов,
наличие хотя бы одной большой буквы, одной маленькой буквы и одной цифры.'''

# import re
#
# passwords = ['Password123', 'password', 'PASSWORD1', 'Passw0rd', 'Passw']
#
# pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'
#
# valid_pas = [pwd for pwd in passwords if re.match(pattern, pwd)]
# print(valid_pas)

'''Напишите программу, которая подсчитывает, сколько раз каждое слово встречается в тексте. Используйте 
collections.Counter.'''

# from collections import Counter
#
# text = 'В этом предложении содержатся слова и слова могут повторяться'
#
# words_list = text.split()
# word_counter = Counter(words_list)
# print(word_counter)

'''Используйте defaultdict, чтобы создать словарь, где значения по умолчанию будут равны пустым спискам.
Затем добавьте несколько ключей и значений в этот словарь.'''

# from collections import defaultdict
#
# def_dic = defaultdict(list)
# data = [('ключ1', 'элемент1'), ('ключ2', 'элемент2'), ('ключ3', 'элемент3')]
#
# for key, val in data:
#     def_dic[key].append(val)
#
# print(def_dic)


'''Используйте collections.deque для реализации очереди задач. Добавьте несколько задач в начало и конец очереди,
затем извлеките их.'''

# from collections import deque
#
# task_deque = deque()
#
# task_deque.append('Task1')
# # 1
# task_deque.appendleft('Task2')
# # 2 1
# task_deque.extend(['Task3', 'Task4'])
# # 2 1 3 4
# task_deque.extendleft(['Task5', 'Task6'])
# # 6 5 2 1 3 4
#
# while task_deque:
#     print(task_deque.popleft())


'''Напишите программу, которая создает случайный пароль длиной 12 символов, в котором используются буквы верхнего
и нижнего регистра, цифры и специальные символы.'''

# import random
# import string
#
# all_symbols = string.ascii_letters + string.digits + string.punctuation
#
# password = ''.join(random.choice(all_symbols) for _ in range(12))
# print(password)


'''Создайте список чисел от 1 до 10 и перемешайте его элементы случайным образом.'''

# import random
#
# numbers_list = list(range(1, 11))
# random.shuffle(numbers_list)
# print(numbers_list)

'''Дан список студентов. Напишите программу, которая случайным образом выбирает одного студента для ответа на
вопрос.'''

import random

students = ["Алексей", "Иван", "Мария", "Ольга", "Екатерина"]

answer_student = random.choice(students)
print(answer_student)


