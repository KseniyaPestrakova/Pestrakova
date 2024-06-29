from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(client_info: str) -> str:
    """Возвращает маску номера карты или счета с частично скрытыми данными"""
    if type(client_info) is not str:
        raise ValueError('Недостаточно информации о карте/счете')
    if "Счет" in client_info:
        account_number = int(client_info[-20:])
        return str("Счет " + get_mask_account(account_number))
    else:
        card_number = int(client_info.replace(" ", "")[-16:])
        return str(client_info[:-16] + get_mask_card_number(card_number))


def get_data(my_date: str) -> str:
    """Возвращает дату в виде ДД.ММ.ГГГГ"""
    if len(my_date) < 10:
        raise ValueError('Недостаточно данных для вывода даты')
    return my_date[8:10] + "." + my_date[5:7] + "." + my_date[:4]
