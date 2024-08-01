from typing import Any

from src.processing import filter_by_search, filter_by_state, sort_by_date
from src.utils import get_list_transactions, get_list_transactions_csv, get_list_transactions_xlsx
from src.widget import get_data, mask_account_card


def main() -> Any:
    """Функция, которая отвечает за основную логику проекта и связывает функциональности между собой."""

    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )

    user_choice_file = input()

    user_file = []
    while user_choice_file not in ["1", "2", "3"]:
        print("Такого пункта нет в меню, попробуйте еще раз\n")
        user_choice_file = input()
    else:
        if user_choice_file == "1":
            print("Для обработки выбран JSON-файл")
            user_file = get_list_transactions("data/operations.json")
        elif user_choice_file == "2":
            print("Для обработки выбран CSV-файл")
            user_file = get_list_transactions_csv("data/transactions.csv")
        elif user_choice_file == "3":
            print("Для обработки выбран XLSX-файл")
            user_file = get_list_transactions_xlsx("data/transactions_excel.xlsx")

    question_status = (
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы:\n"
        "EXECUTED, CANCELED, PENDING"
    )

    user_choice_status = input(f"{question_status}\n").upper()
    while user_choice_status not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f'Статус операции "{user_choice_status}" недоступен.\n')
        user_choice_status = input(f"{question_status}").upper()
    else:
        print(f'Операции отфильтрованы по статусу "{user_choice_status}"')
        filter_status_transactions = filter_by_state(user_file, user_choice_status)

    question_sort_date = "Отсортировать операции по дате? Да/Нет\n"
    user_choice_sort_date = input(f"{question_sort_date}").lower()

    if user_choice_sort_date == "да":
        question_sort_date_reverse = "Отсортировать по возрастанию или по убыванию?\n"
        user_choice_sort_date_reverse = input(f"{question_sort_date_reverse}").lower()
        while user_choice_sort_date_reverse not in ["по возрастанию", "по убыванию"]:
            print(f"Невозможно отсортировать по {user_choice_sort_date_reverse}")
            user_choice_sort_date_reverse = input(f"{question_sort_date_reverse}").lower()
        else:
            if user_choice_sort_date_reverse == "по возрастанию":
                filter_status_and_date_transactions = sort_by_date(filter_status_transactions, False)
            else:
                filter_status_and_date_transactions = sort_by_date(filter_status_transactions, True)
    else:
        filter_status_and_date_transactions = filter_status_transactions

    question_currency = "Выводить только рублевые транзакции? Да/Нет\n"
    user_choice_currency = input(f"{question_currency}").lower()
    if user_choice_currency == "да":
        try:
            filter_rub_transactions = [
                transaction
                for transaction in filter_status_and_date_transactions
                if transaction["currency_code"] == "RUB"
            ]
        except KeyError:
            filter_rub_transactions = [
                transaction
                for transaction in filter_status_and_date_transactions
                if transaction["operationAmount"]["currency"]["code"] == "RUB"
            ]

    else:
        filter_rub_transactions = filter_status_and_date_transactions

    question_search = "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
    user_choice_search = input(f"{question_search}").lower()
    if user_choice_search == "да":
        search_list = input("Введите слово для поиска:")
        filter_rub_transactions_search = filter_by_search(filter_rub_transactions, search_list)
    else:
        filter_rub_transactions_search = filter_rub_transactions

    if len(filter_rub_transactions_search) >= 1:
        print(f"Всего банковских операций в выборке: {len(filter_rub_transactions_search)}\n")

        for transaction in filter_rub_transactions_search:
            # count_from_curd = [too['to'] for too in filter_rub_transactions_search]
            # count_to_curd = [too['from'] for too in filter_rub_transactions_search]

            if transaction["description"] == "Открытие вклада":
                date = get_data(transaction["date"])
                print(f"{date} {transaction['description']}")
                print(f"{mask_account_card(str(transaction['to']))}")

            else:
                date = get_data(transaction["date"])
                print(f"{date} {transaction['description']}")
                print(
                    f"{mask_account_card(str(transaction['from']))} ->" f" {mask_account_card(str(transaction['to']))}"
                )

            try:
                if transaction["currency_code"] == "RUB":
                    currency_code = "руб."
                    print(f"Сумма: {round(transaction['amount'], 0)} {currency_code}\n")
                else:
                    print(f"Сумма: {round(transaction['amount'], 0)} {transaction['currency_code']}\n")
            except KeyError:
                print(
                    f"Сумма: {round(float(transaction['operationAmount']['amount']), 0)} "
                    f"{transaction['operationAmount']['currency']['name']}\n"
                )
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    return


if __name__ == "__main__":
    result = main()
    print(result)
