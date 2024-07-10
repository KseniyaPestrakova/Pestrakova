'''Напишите функцию generate_users(first_names, last_names, cities), которая будет генерировать случайных
пользователей. Функция должна возвращать генератор, который будет выдавать каждого пользователя по одному
в виде словаря.
Сгенерируйте группу пользователей и выведите ее списком в консоль в формате JSON.'''


import random
import json


# first_names = ['Ann', 'Mary', 'Jon', 'Andrey', 'Max', 'Alex']
# last_names = ['Black', 'White', 'King', 'Jakson', 'Bridgerton']
# cities = ['Moscow', 'Dubai', 'NY', 'Paris']
# def generate_users(first_names, last_names, cities):
#     while True:
#         user = {
#             'first_name': random.choice(first_names),
#             'last_name': random.choice(last_names),
#             'age': random.randint(18, 65),
#             'city': random.choice(cities)
#         }
#         yield user
#
# if __name__ == '__main__':
#     users = generate_users(first_names, last_names, cities)
#
#     user_group1 = [next(users) for i in range(4)]
#     user_group2 = [next(users) for i in range(6)]
#
#     print('User group #1')
#     print(json.dumps(user_group1, indent=4))
#     print('User group #2')
#     print(json.dumps(user_group2, indent=4))



# import pytest
#
#
# @pytest.fixure
# def cities():
#     return ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
#
#
# def test_generate_users_num_users(cities):
#     """Проверяет, что количество сгенерированных пользователей равно запрошенному количеству пользователей."""
#
#     num_users = 5
#     assert len(list(generate_users(num_users, cities))) == num_users
#
#
# def test_generate_users_keys(cities):
#     """Проверяет, что у всех сгенерированных пользователей есть правильные ключи."""
#
#     for user in generate_users(5, cities):
#         assert set(user.keys()) == {'first_name', 'last_name', 'age', 'city'}
#
#
# def test_generate_users_first_names(cities):
#     """Проверяет, что у всех сгенерированных пользователей имя является одним из возможных имен."""
#
#     first_names = ['John', 'Jane', 'Mark', 'Emily', 'Michael', 'Sarah']
#     for user in generate_users(5, cities):
#         assert user['first_name'] in first_names
#
#
# def test_generate_users_last_names(cities):
#     """Проверяет, что у всех сгенерированных пользователей фамилия является одной из возможных фамилий."""
#
#     last_names = ['Doe', 'Smith', 'Johnson', 'Brown', 'Lee', 'Wilson']
#     for user in generate_users(5, cities):
#         assert user['last_name'] in last_names
#
#
# def test_generate_users_age(cities):
#     """Проверяет, что у всех сгенерированных пользователей возраст находится в заданном диапазоне."""
#
#     for user in generate_users(5, cities):
#         assert 18 <= user['age'] <= 65
#
#
# def test_generate_users_cities(cities):
#     """Проверяет, что у всех сгенерированных пользователей город является одним из возможных городов."""
#
#     for user in generate_users(5, cities):
#         assert user['city'] in cities


'''Напишите программу, которая будет принимать на вход JSON-файл с данными о финансовых транзакциях,
фильтровать транзакции, совершенные в определенной валюте, и сохранять отфильтрованные данные в новый JSON-файл.
Также напишите декоратор, который будет выводить в консоль статистику по количеству отфильтрованных транзакций.
Статистика должна включать в себя количество отфильтрованных транзакций и их суммарную стоимость.'''




# def decorator_currency(func):
#     def wrapper(*args, **kwargs):
#         filtered_transactions = func(*args, **kwargs)
#         total_amount = sum([transaction['amount'] for transaction in filtered_transactions])
#         print(f"Отфильтровано {len(filtered_transactions)} транзакций на сумму {total_amount}")
#         return filtered_transactions
#     return wrapper
#
#
# @decorator_currency
# def filter_transactions_by_currency(input_file, output_file, currency):
#     """Фильтрует транзакции по валюте и сохраняет результат в новый файл."""
#
#     with open(input_file, 'r') as f:
#         transactions = json.load(f)
#
#     filtered_transactions = [transaction for transaction in transactions if transaction['currency'] == currency]
#
#     with open(output_file, 'w') as f:
#         json.dump(filtered_transactions, f, indent=4)
#
#     return filtered_transactions
#
#
# def main():
#     input_file = 'transactions.json'
#     output_file = 'transactions_filtered.json'
#     currency = 'USD'
#
#     filtered_transactions = filter_transactions_by_currency(input_file, output_file, currency)
#     print(filtered_transactions)
#
# if __name__ == '__main__':
#     main()



import requests

# payload = {'my_key': 'my_value'}
# r = requests.post('https://httpbin.org/post', data=payload)
#
# print(r.text)


# Задаем адрес сайта, к которому хотим обратиться
# url = "https://example.com"
#
# # Выполняем GET-запрос к сайту и сохраняем ответ в переменную response
# response = requests.get(url)
#
# # Получаем статус-код из ответа и выводим его на экран
# status_code = response.status_code
# print(f"Статус код: {status_code}")
#
# # Проверяем, равен ли статус-код 200, то есть чтобы запрос был успешным
# if status_code == 200:
#     # Выводим содержимое сайта на экран
#     content = response.text
#     print(f"Содержимое сайта:\n{content}")
# else:
#     # Выводим сообщение об ошибке
#     print(f"Запрос не был успешным. Возможная причина: {response.reason}")


# import os
# from dotenv import load_dotenv
# import requests
#
# # Загрузка переменных из .env-файла
# load_dotenv()
#
# # Получение значения переменной GITHUB_TOKEN из .env-файла
# github_token = os.getenv('GITHUB_TOKEN')
#
# # Создание заголовка с токеном доступа API
# headers = {
#     'Authorization': f'token {github_token}'
#     }
#
# # Отправка GET-запроса к API
# response = requests.get('https://api.github.com/user', headers=headers)
#
# # Обработка ответа
# print(response.json())
#
#
#
# from unittest.mock import Mock
#
# def test_get_random_number():
#     mock_random = Mock(return_value=5)
#     random.randint = mock_random
#     assert get_random_number() == 5
#     mock_random.assert_called_once_with(0, 10)
#
#
#
#
# from unittest.mock import patch
# import random
#
# def get_random_number():
#     return random.randint(0, 10)
#
# @patch('random.randint')
# def test_get_random_number(mock_random):
#     mock_random.return_value = 5
#     assert get_random_number() == 5
#     mock_random.assert_called_once_with(0, 10)
#
#
# '''Напишите программу, которая получает информацию о репозиториях пользователей GitHub.Программа должна иметь
# следующую функциональность: Принимает на вход список пользователей GitHub.Для каждого пользователя получает
# его информацию и список его репозиториев. Составляет список результатов в формате JSON, в котором для каждого
# пользователя указаны его логин, количество публичных репозиториев и список его репозиториев.Для получения информации
# о пользователе и его репозиториях должны использоваться открытые API GitHub.'''
#
# import json
#
# import requests
#
# def get_github_users(users):
#     results = []
#     for user in users:
#         status, user_data = get_user_info(user)
#         if not status:
#             continue
#
#         status, repositories = get_user_repos(user)
#         if not status:
#             continue
#
#         result = {
#             'login': user_data['login'],
#             'public_repos': user_data['public_repos'],
#             'repositories': repositories
#         }
#         results.append(result)
#     return json.dumps(results)
#
# def get_user_info(user: str) -> tuple[bool, dict]:
#     url = f"https://api.github.com/users/{user}"
#     response = requests.get(url)
#     if response.status_code != 200:
#         return False, {}
#     return True, response.json()
#
# def get_user_repos(user: str) -> tuple[bool, list]:
#     repo_url = f"https://api.github.com/users/{user}/repos"
#     repo_response = requests.get(repo_url)
#     if repo_response.status_code != 200:
#         return False, []
#     return True, [repo['name'] for repo in repo_response.json()]
#
#
#
# #ТЕСТЫ
# import json
# from unittest.mock import patch
#
# from src.github import get_user_info, get_user_repos, get_github_users
#
# @patch('src.github.requests.get')
# def test_get_user_info(mocked_get):
#     mocked_get.return_value.status_code = 200
#     mocked_get.return_value.json.return_value = {'login': 'test_user', 'public_repos': 10}
#     result = get_user_info('test_user')
#     assert result == (True, {'login': 'test_user', 'public_repos': 10})
#
# @patch('src.github.requests.get')
# def test_get_user_info_invalid(mocked_get):
#     mocked_get.return_value.json.return_value = {'message': 'Not Found'}
#     result = get_user_info('non_existent_user')
#     assert result == (False, {})
#
# @patch('src.github.requests.get')
# def test_get_user_repos(mocked_get):
#     mocked_get.return_value.status_code = 200
#     mocked_get.return_value.json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]
#     result = get_user_repos('test_user')
#     assert result == (True, ['repo1', 'repo2'])
#
# @patch('src.github.requests.get')
# def test_get_user_repos_invalid(mocked_get):
#     mocked_get.return_value.status_code = 404
#     mocked_get.return_value.json.return_value = {'message': 'Not Found'}
#     result = get_user_repos('non_existent_user')
#     assert result == (False, [])
#
# @patch('src.github.get_user_info')
# @patch('src.github.get_user_repos')
# def test_get_github_users(mock_get_user_repos, mock_get_user_info):
#     mock_get_user_info.return_value = (True, {'login': 'user1', 'public_repos': 2})
#     mock_get_user_repos.return_value = (True, ['repo1', 'repo2'])
#     expected_result = [{'login': 'user1', 'public_repos': 2, 'repositories': ['repo1', 'repo2']}]
#     result = get_github_users(['user1'])
#     assert result == json.dumps(expected_result)
#
# @patch('src.github.get_user_info')
# @patch('src.github.get_user_repos')
# def test_get_github_users_negative(mock_get_user_repos, mock_get_user_info):
#     mock_get_user_info.return_value = (False, {})
#     mock_get_user_repos.return_value = (False, [])
#     result = get_github_users(['non_existent_user'])
#     assert result == '[]'
#
#
#
#
# '''Напишите функцию, которая будет получать курс валюты на заданную дату из API ЦБ РФ и возвращать его в формате JSON.
# Используйте сайт https://www.cbr-xml-daily.ru/daily_json.js.
# Пример вызова функции:
# rate = get_currency_rate("USD")
# print(rate)
# Результат:
# {    "currency_code": "USD",    "rate": 72.7384}'''
#
#
# import requests
#
# def get_currency_rate(date, currency_code):
#     url = f"https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js"
#     response = requests.get(url)
#     if response.status_code != 200:
#         raise ValueError(f"Failed to get currency rate for date {date}")
#     data = response.json()
#     currency_data = data["Valute"].get(currency_code)
#     if not currency_data:
#         raise ValueError(f"No data for currency {currency_code}")
#     return {
#         "date": date,
#         "currency_code": currency_code,
#         "rate": currency_data["Value"],
#     }
#
#
# #ТЕСТЫ
# def test_get_currency_rate(requests_mock):
#     date = "2021-10-29"
#     currency_code = "USD"
#
#     requests_mock.get(
#         f"https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js",
#         json={
#             "Valute": {
#                 "USD": {"Value": 72.5},
#                 "EUR": {"Value": 84.8},
#             },
#         },
#     )
#
#     rate = get_currency_rate(date, currency_code)
#
#     assert requests_mock.call_count == 1
#     assert rate == {
#         "date": date,
#         "currency_code": currency_code,
#         "rate": 72.5,
#     }
#
#     currency_code = "GBP"
#
#     with pytest.raises(ValueError, match="No data for currency GBP"):
#         rate = get_currency_rate(date, currency_code)
#
#     requests_mock.get(
#         f"https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js",
#         status_code=404,
#     )
#
#     with pytest.raises(ValueError, match=f"Failed to get currency rate for date {date}"):
#         rate = get_currency_rate(date, currency_code)
#
#
#
#     '''Напишите функцию, которая принимает список дат в формате списка строк, например
# ["2022.12.31", "2023.1.7"], и возвращает список дат в формате строк через одну неделю, например
# ["January 7, 2023", "January 14, 2023"].'''
#
# from datetime import datetime, timedelta
#
# def add_week_to_dates(dates: list[str]) -> list[str]:
#     output_dates = []
#     for date in dates:
#         date_obj = datetime.strptime(date, '%Y.%m.%d')
#         new_date_obj = date_obj + timedelta(days=7)
#         output_dates.append(new_date_obj.strftime('%B %#d, %Y'))
#     return output_dates
#
#
# #Тесты:
# from src.code import add_week_to_dates
#
# def test_add_week_to_dates():
#     assert add_week_to_dates(["2022.12.31", "2023.1.7"]) == ["January 7, 2023", "January 14, 2023"]
#     assert add_week_to_dates([]) == []
#
#
# '''Напишите функцию, которая принимает JSON-строку с данными о различных событиях, включающих даты начала
#  и окончания, и возвращает список длительностей каждого события в днях.
# Пример входных данных:
# [  {    "name": "Event 1",
#     "start_date": "2022-01-01",
#     "end_date": "2022-01-05"  },
#       {    "name": "Event 2",
#     "start_date": "2022-02-15",
#     "end_date": "2022-02-18"  },
#   {    "name": "Event 3",
#     "start_date": "2022-03-10",
#     "end_date": "2022-03-20"  }]
# Пример выходных данных: [5, 4, 11]'''
#
#
# import json
# from datetime import datetime
#
# def event_durations(json_str):
#     events = json.loads(json_str)
#     durations = []
#     for event in events:
#         start_date = datetime.strptime(event['start_date'], '%Y-%m-%d')
#         end_date = datetime.strptime(event['end_date'], '%Y-%m-%d')
#         duration = (end_date - start_date).days
#         durations.append(duration)
#     return durations
#
#
# #Тесты:
# def test_event_durations():
#     json_str = '[{"name": "Event 1", "start_date": "2022-01-01", "end_date": "2022-01-05"}, {"name": "Event 2", "start_date": "2022-02-15", "end_date": "2022-02-18"}, {"name": "Event 3", "start_date": "2022-03-10", "end_date": "2022-03-20"}]'
#     assert event_durations(json_str) == [4, 3, 10]


'''Написать функцию, которая будет принимать путь до файла и название города и выполнять следующие действия:
Прочитать JSON-файл с данными о погоде в формате JSON.
Выбрать из этого файла данные для города, который введет пользователь.
Рассчитать среднюю температуру за неделю для выбранного города.
Записать результат расчета в новый JSON-файл.'''


import json


# def get_avg_for_city(path: str, city: str) -> bool:
#     '''Получение средней температуры за неделю для города'''
#     try:
#         with open(path) as city_file:
#             try:
#                 city_data = json.load(city_file)
#             except json.JSONDecodeError:
#                 print('Ошибка декодирования файла')
#                 return False
#     except FileNotFoundError:
#         print('Файл не найден')
#         return False
#
#     avg_temp = round(sum(city_data[city].values()) / len(city_data[city].values()), 2)
#     out_data = {city: {'Average temperature': avg_temp}}
#     with open('out.json', 'w') as out_file:
#         json.dump(out_data, out_file)
#
#     return True

# if __name__ == '__main__':
#     get_avg_for_city('data.json', 'Moscow')



'''Напишите функцию get_days_between_dates(date1, date2), которая принимает на вход две даты в формате 
"dd.mm.yyyy" и возвращает количество дней между ними.
Пример использования функции:

>>> get_days_between_dates("01.01.2022", "31.01.2022")
30'''

# import datetime
#
#
# def get_days_between_dates(date1: str, date2: str) -> int:
#     '''получить кол-во дней между датами'''
#     date1_obj = datetime.datetime.strptime(date1, '%d.%m.%Y')
#     date2_obj = datetime.datetime.strptime(date2, '%d.%m.%Y')
#
#     date_diff = (date2_obj - date1_obj).days
#
#     return date_diff
#
#
# if __name__ == '__main__':
#     print(get_days_between_dates("01.01.2022", "31.01.2022"))


'''Напишите функцию с названием get_github_repos(username: str) -> list[str], которая принимает на вход имя
 пользователя GitHub и возвращает список названий репозиториев этого пользователя.
Для выполнения задания необходимо использовать следующие этапы:

Сделать GET-запрос к API GitHub, используя следующий URL: 
https://api.github.com/users/{username}/repos
Обработать ответ и извлечь из него названия репозиториев.
Вернуть список названий репозиториев.
Если пользователь с указанным именем не найден, функция должна вернуть пустой список.

Пример использования:

repos = get_github_repos('octocat')
print(repos)'''


def get_github_repos(username: str) -> list[str]:
    '''Получение списка репозиториев пользователя'''
    response = requests.get(f'https://api.github.com/users/{username}/repos')
    if response.status_code == 200:
        repos = [repo['full_name'] for repo in response.json()]
    else:
        repos = []

    return repos


if __name__ == '__main__':
    repos = get_github_repos('octocat')
    print(repos)


