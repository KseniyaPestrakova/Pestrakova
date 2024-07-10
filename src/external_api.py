import os
from dotenv import load_dotenv
import requests


def get_summ_transactions_rub(transaction: dict) -> float:
    '''Возвращает сумму транзакции в рублях'''

    amount = transaction["operationAmount"]["amount"]

    if transaction["operationAmount"]["currency"]["code"] != "RUB":
        currency = transaction["operationAmount"]["currency"]["code"]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        load_dotenv()
        API_KEY = os.getenv('API_KEY')
        payload = {}
        headers = {"apikey": API_KEY}

        response = requests.request("GET", url, headers=headers, data=payload)

        data = response.json()
        result = data['result']
        return result
    else:
        return amount


if __name__ == '__main__':
    ref = get_summ_transactions_rub({
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
  })
    print(ref)

