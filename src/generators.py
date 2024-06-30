from typing import Generator


def filter_by_currency(transactions: list, currency: str) -> Generator:
    """Выводит из списка операций по очереди операции, в которых указана соответсвующая валюта"""
    n = 0
    while True:
        my_list = list(
            (transact for transact in transactions if transact["operationAmount"]["currency"]["code"] == currency)
        )
        yield my_list[n]
        n += 1


def transaction_descriptions(transactions: list) -> Generator:
    """Выводит описание каждой операции из списка операций по очереди"""
    n = 0
    while True:
        my_list = list((transact["description"] for transact in transactions))
        yield my_list[n]
        n += 1


def card_number_generator(start: int, stop: int) -> Generator:
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне"""
    for number in range(start, stop + 1):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number
        formatted_card_number = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
        yield formatted_card_number
