import json
import logging
from typing import Any
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    filename="..\\logs\\utils.log",
    filemode="w",
)

utils_logger = logging.getLogger("utils")


def get_list_transactions(path: str) -> list:
    """Получаем список словарей с данными о финансовых транзакциях из JSON-файла"""
    utils_logger.info("Starting func get_list_transactions")
    try:
        utils_logger.info(f"Open file {path}")
        with open(path, "r", encoding="utf-8") as file:
            try:
                list_transactions: list[Any] = json.load(file)
                utils_logger.info(f"Return list_transactions from {path}")
                return list_transactions
            except json.JSONDecodeError:
                utils_logger.error("Problems with JSON file")
                list_transactions_error: list[Any] = []
                return list_transactions_error
    except FileNotFoundError:
        utils_logger.error(f"File {path} not found")
        list_transactions_notfound_error: list[Any] = []
        return list_transactions_notfound_error


def get_list_transactions_csv(path: str) -> list:
    '''Получаем список словарей с данными о финансовых транзакциях из csv-файла'''
    utils_logger.info("Starting func get_list_transactions_csv")
    try:
        df = pd.read_csv(path, delimiter=';')
        list_transactions = df.to_dict(orient='records')
        utils_logger.info(f"Return list_transactions from {path}")
        return list_transactions
    except Exception:
        utils_logger.error(f"Something wrong with csv-file {path}")
        list_transactions = []
        return list_transactions


def get_list_transactions_xlsx(path: str) -> list:
    '''Получаем список словарей с данными о финансовых транзакциях из excel-файла'''
    utils_logger.info("Starting func get_list_transactions_xlsx")
    try:
        df_excel = pd.read_excel(path)
        list_transactions = df_excel.to_dict(orient='records')
        utils_logger.info(f"Return list_transactions from {path}")
        return list_transactions
    except Exception:
        utils_logger.error(f"Something wrong with excel-file {path}")
        list_transactions = []
        return list_transactions


if __name__ == '__main__':
    result = get_list_transactions_xlsx('..\\data\\transactions_excel.xlsx')
    print(result)
