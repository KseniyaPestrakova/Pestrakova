def get_mask_card_number(card_number: int) -> str:
    """возвращает маску номера карты в формате XXXX XX** **** XXXX"""
    return str(card_number)[:4] + " " + str(card_number)[4:6] + "** **** " + str(card_number)[-4:]


print(get_mask_card_number(7000792289606361))


def get_mask_account(account_number: int) -> str:
    """возвращает маску номера счета в формате **XXXX"""
    return "**" + str(account_number)[-4:]


print(get_mask_account(73654108430135874305))
