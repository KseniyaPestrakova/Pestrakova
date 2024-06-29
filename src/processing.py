from typing import Any, Dict, List


def filter_by_state(list_dict: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует операции по ключу state"""
    result_list = list()
    for dictionary in list_dict:
        if dictionary["state"] == state:
            result_list.append(dictionary)
    return result_list


def sort_by_date(list_dict_dates: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Функция сортировки операций по дате"""
    return sorted(list_dict_dates, key=lambda dictionary_dates: dictionary_dates["date"], reverse=reverse)
