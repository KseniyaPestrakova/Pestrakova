import json
from typing import Any


def get_list_transactions(path: str) -> list:
    """Получаем список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as file:
            try:
                list_transactions: list[Any] = json.load(file)
                return list_transactions
            except json.JSONDecodeError:
                list_transactions_error: list[Any] = []
                return list_transactions_error
    except FileNotFoundError:
        list_transactions_notfound_error: list[Any] = []
        return list_transactions_notfound_error

