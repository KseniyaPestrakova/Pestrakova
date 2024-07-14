'''Необходимо создать приложение, которое позволит получить вакансии с сайта hh.ru за текущий день по API.

При запуске приложения берется текущая дата, после чего извлекаются вакансии, опубликованные на hh.ru за этот день.
Все данные о вакансиях выгружаются в JSON-файл.
В файле содержится только основная информация:
название вакансии;
зарплатная вилка (зарплата от и зарплата до);
ссылка на вакансию.
В приложении предусмотрены возможности указать, какие слова должны содержаться в вакансии, а также список слов,
которые исключают вакансии, их содержащие.
Название JSON-файла формируется автоматически:
сначала указывается дата запроса;
после чего добавляются слова, указанные в запросе, разделенные нижним подчеркиванием.
Необходимо также добавить логирование различных кейсов в программе.'''

# import logging
#
# import requests
#
# logger = logging.getLogger(__name__)
#
#
# def get_vacancies(search_text, exclude_text):
#     url = 'https://api.hh.ru/vacancies'
#     params = {
#         'text': search_text,
#         'exclude': exclude_text,
#         'search_field': 'name',
#         'area': 1,
#         'period': 1,
#         'only_with_salary': True,
#         'per_page': 100,
#         'page': 0
#     }
#
#     vacancies = []
#     while True:
#         response = requests.get(url, params=params)
#         data = response.json()
#         vacancies += data['items']
#
#         if data['pages'] == params['page']:
#             break
#         else:
#             params['page'] += 1
#
#     result = []
#     for vacancy in vacancies:
#         vacancy_data = {
#             'name': vacancy['name'],
#             'salary': vacancy['salary']['from'] if vacancy['salary']['from'] is not None else 'Not specified',
#             'url': vacancy['url']
#         }
#         result.append(vacancy_data)
#
#     logger.info(f"Found {len(result)} vacancies")
#     return result
#
# from datetime import datetime
#
# from parser import get_vacancies
# from file_manager import save_to_json
# from logger import setup_logging
# from config import SEARCH_TEXT, EXCLUDE_TEXT
#
# logger = setup_logging()
#
# if __name__ == "__main__":
#     logger.info("Application starts....")
#
#     date_today = datetime.now().strftime("%Y_%m_%d")
#     file_name = f"{date_today}_{SEARCH_TEXT.replace(' ', '_')}.json"
#
#     vacancies = get_vacancies(SEARCH_TEXT, EXCLUDE_TEXT)
#     save_to_json(vacancies, file_name)
#
#     logger.info("Application finished")
#
#
#
# import logging
#
#
# def setup_logging():
#     logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     return logging.getLogger()
#
#
# import json
# import logging
# import os
#
# logger = logging.getLogger(__name__)
#
#
# def save_to_json(data, file_name):
#     with open(file_name, 'w', encoding='utf-8') as file:
#         json.dump(data, file, ensure_ascii=False, indent=4)
#
#     logger.info(f"Data successfully saved to {os.getcwd()}\\{file_name}")
#
#
# SEARCH_TEXT = 'Python developer'
# EXCLUDE_TEXT = 'Junior Middle Senior'

'''Напишите функцию, которая получает список пользователей из API, сохраняет его в JSON-файл и добавляет в файл логов дату и время запроса.
Ссылка на API: https://jsonplaceholder.typicode.com/users.

Пример содержимого файла 
log.txt
:

INFO:root:Request time: 2022-10-22 14:30:05
INFO:root:Request time: 2022-10-22 14:45:12'''


# import requests
# import logging
# import json
#
# logging.basicConfig(
#     filename='application.log',
#     filemode='a+',
#     format='%(levelname)s:%(name)s:Request time: %(asctime)s',
#     level=logging.INFO
# )
#
# logger = logging.getLogger()
#
#
# URL = 'https://jsonplaceholder.typicode.com/users'
#
# def get_users_and_save() -> None:
#     '''Получение пользователей и сохранение в файл'''
#     response = requests.get(URL)
#     logger.info('Done')
#     with open('users.json', 'w') as users_file:
#         json.dump(response.json(), users_file)
#
#
# if __name__ == '__main__':
#     get_users_and_save()


'''У вас есть API: https://jsonplaceholder.typicode.com/photos.
Напишите приложение, которое скачивает картинки заданного альбома и сохраняет в директории photos. Все шаги должны
логироваться: от старта приложения до вывода текущего состояния и информации о завершении приложения и общем количестве
скачанных картинок.
Требования:
Все шаги приложения должны выводиться в консоль, для этого нужно использовать logging.
Приложение должно принимать аргументы: 
album_id  (обязательный) и limit  (необязательный, по умолчанию 100).
Приложение должно скачивать картинки по одной и выводить каждую в консоль с указанием имени файла и номера текущей
картинки. В конце работы приложения должна выводиться информация о завершении работы и общем количестве скачанных
картинок.
Пример вывода логов в консоль:

INFO:root:Starting app...
INFO:root:Downloading album 1 images...
INFO:root:Saving image 1 to photos/1-1.jpg
INFO:root:Saving image 2 to photos/1-2.jpg
INFO:root:Finished downloading images. Total images downloaded: 2'''


import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s:%(name)s:%(message)s'
)

logger = logging.getLogger()

URL = 'https://jsonplaceholder.typicode.com/photos'


def get_photos_from_album(album_id: int, limit: int = 20) -> None:
    '''Скачать фото по заданному альбому'''
    logger.info('Starting app...')
    response = requests.get(URL)
    counter = 1
    logger.info(f'Downloading album {album_id} images...')
    for item in response.json():
        if item.get('albumId') == album_id:
            image_url = item.get('url')
            image_data = requests.get(image_url)
            logger.info(f'Saving image {counter} to photos/{album_id}-{counter}.png')
            with open(f'{album_id}-{counter}.png', 'wb') as image_file:
                image_file.write(image_data.content)
            counter += 1
            if counter > limit:
                break


if __name__ == '__main__':
    get_photos_from_album(1, 5)
