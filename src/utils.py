import json


def get_list_transactions(path: str) -> list:
    '''Получаем список словарей с данными о финансовых транзакциях'''
    try:
        with open(path, 'r', encoding='utf-8') as file:
            try:
                list_transactions = json.load(file)
                return list_transactions
            except json.JSONDecodeError:
                list_transactions = []
                return list_transactions
    except FileNotFoundError:
        list_transactions = []
        return list_transactions




