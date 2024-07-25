import re
from collections import Counter
from typing import Any, Dict, List

from src.utils import get_list_transactions


def filter_by_state(list_dict: List[Dict[str, Any]], my_state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует операции по ключу state"""

    result_list = [dictionary for dictionary in list_dict if dictionary.get("state") == my_state]
    return result_list


def sort_by_date(list_dict_dates: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Функция сортировки операций по дате"""
    return sorted(list_dict_dates, key=lambda dictionary_dates: dictionary_dates["date"], reverse=reverse)


def filter_by_search(list_operations: List[Dict[str, Any]], search_description: str) -> List[Dict[str, Any]]:
    """Функция поиска операций, у которых в описании есть заданная строка"""
    return [operation for operation in list_operations if re.search(search_description, operation["description"])]


def filter_by_category_and_amount(list_operations: List[Dict[str, Any]], categorys: list) -> Dict:
    """Функция, считающая кол-во операций в каждой категории из заданного списка категорий"""
    category_list = []
    for operation in list_operations:
        if operation["description"] in categorys:
            category_list.append(operation["description"])
        else:
            continue
    category_counted = Counter(category_list)
    category_dict = dict(category_counted.items())
    for category in categorys:
        if category not in category_dict:
            category_dict[category] = 0
        else:
            continue
    return category_dict


if __name__ == "__main__":
    list123 = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Поступление",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Поступление",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
    ]
    list_json = get_list_transactions("../data/operations.json")

    # print(filter_by_category_and_amount(list123, ['Возврат', 'Перевод организации']))
    print(filter_by_state(list123, "EXECUTED"))
