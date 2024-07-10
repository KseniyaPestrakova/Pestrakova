from unittest.mock import patch
from src.external_api import get_summ_transactions_rub


@patch('requests.request')
def test_get_summ_transactions(mock_get):
    '''Проверяем, что в валюте сумма выводится в пересчете на рубли'''
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'success': True,
                                               'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37},
                                               'info': {'timestamp': 1720647244, 'rate': 88.350156},
                                               'date': '2024-07-10', 'result': 726359.322034}
    mock_get.get.return_value = mock_get
    transaction = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }
    assert get_summ_transactions_rub(transaction) == 726359.32


def test_get_summ_transactions_rub():
    '''Проверяем вывод суммы в рублях'''
    transaction = {
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
    assert get_summ_transactions_rub(transaction) == 31957.58
