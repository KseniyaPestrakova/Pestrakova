from src.utils import get_list_transactions, get_list_transactions_csv, get_list_transactions_xlsx
from unittest.mock import patch

import pandas as pd


def test_get_list_transactions_wrong():
    '''Проверка на неверный путь/несуществующий json-файл'''
    assert get_list_transactions('operations.json') == []


def test_get_list_transactions():
    ''''Проверка, если указан корректный путь к json файлу'''
    assert get_list_transactions("..\\data\\operations.json")[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }


@patch('tests.test_utils.pd.read_csv')
def test_get_list_transactions_csv_wrong(mock_read_csv):
    '''Проверка на неверный путь/несуществующий csv-файл'''
    mock_read_csv.return_value = pd.DataFrame()
    assert get_list_transactions_csv('path') == []


def test_get_list_transactions_csv():
    '''Проверка c существующим csv-файлом'''
    assert get_list_transactions_csv('..\\data\\transactions.csv')[0] == {'id': 650703.0, 'state': 'EXECUTED',
                                                                          'date': '2023-09-05T11:30:32Z',
                                                                          'amount': 16210.0, 'currency_name': 'Sol',
                                                                          'currency_code': 'PEN',
                                                                          'from': 'Счет 58803664561298323391',
                                                                          'to': 'Счет 39745660563456619397',
                                                                          'description': 'Перевод организации'}


@patch('tests.test_utils.pd.read_excel')
def test_get_list_transactions_xlsx_wrong(mock_read_xlsx):
    '''Проверка на неверный путь/несуществующий excel-файл'''
    mock_read_xlsx.return_value = pd.DataFrame()
    assert get_list_transactions_xlsx('path') == []


def test_get_list_transactions_xlsx():
    '''Проверка c существующим excel-файлом'''
    assert get_list_transactions_xlsx("..\\data\\transactions_excel.xlsx")[0] == {'id': 650703.0, 'state': 'EXECUTED',
                                                                                  'date': '2023-09-05T11:30:32Z',
                                                                                  'amount': 16210.0,
                                                                                  'currency_name': 'Sol',
                                                                                  'currency_code': 'PEN',
                                                                                  'from': 'Счет 58803664561298323391',
                                                                                  'to': 'Счет 39745660563456619397',
                                                                                  'description': 'Перевод организации'}
