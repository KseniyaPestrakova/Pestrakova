import os

import requests
from dotenv import load_dotenv


def get_summ_transactions_rub(transaction: dict) -> float | str:
    """Возвращает сумму транзакции в рублях"""

    amount = transaction["operationAmount"]["amount"]

    if transaction["operationAmount"]["currency"]["code"] != "RUB":
        currency = transaction["operationAmount"]["currency"]["code"]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        load_dotenv()
        API_KEY = os.getenv("API_KEY")
        payload: dict = {}
        headers = {"apikey": API_KEY}

        response = requests.request("GET", url, headers=headers, data=payload)

        data = response.json()
        result = data["result"]
        if response.status_code == 200:
            return float(round(result, 2))
        else:
            print(f"Запрос не был успешным. Возможная причина: {response.reason}")
            return response.reason
    else:
        return float(amount)
