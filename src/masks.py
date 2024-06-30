def get_mask_card_number(card_number: int) -> str:
    """Возвращает маску номера карты в формате XXXX XX** **** XXXX"""
    if len(str(card_number)) != 16:
        raise ValueError("Номер карты должен состоять из 16 цифр")
    return str(card_number)[:4] + " " + str(card_number)[4:6] + "** **** " + str(card_number)[-4:]


def get_mask_account(account_number: int) -> str:
    """Возвращает маску номера счета в формате **XXXX"""
    if len(str(account_number)) != 20:
        raise ValueError("Номер карты должен состоять из 16 цифр")
    return "**" + str(account_number)[-4:]
