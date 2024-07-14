import json
import logging
from typing import Any

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="..\\logs\\utils.log",
    filemode="w",
)

logger = logging.getLogger("utils")


def get_list_transactions(path: str) -> list:
    """Получаем список словарей с данными о финансовых транзакциях"""
    logger.info("Starting func get_list_transactions")
    try:
        logger.info(f"Open file {path}")
        with open(path, "r", encoding="utf-8") as file:
            try:
                list_transactions: list[Any] = json.load(file)
                logger.info(f"Return list_transactions from {path}")
                return list_transactions
            except json.JSONDecodeError:
                logger.error("Problems with JSON file")
                list_transactions_error: list[Any] = []
                return list_transactions_error
    except FileNotFoundError:
        logger.error(f"File {path} not found")
        list_transactions_notfound_error: list[Any] = []
        return list_transactions_notfound_error
