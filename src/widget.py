from masks import get_mask_card_number
from masks import get_mask_account

def mask_account_card(client_info: str) -> str:
    '''Возвращает маску номера карты или счета с частично скрытыми данными'''
    if 'Счет' in client_info:
        account_number = int(client_info[-20:])
        return 'Счет ' + get_mask_account(account_number)
    else:
        card_number = int(client_info.replace(' ', '')[-16:])
        return str(client_info[:-16]) + get_mask_card_number(card_number)

print(mask_account_card('Счет 64686473678894779589'))
print(mask_account_card('MasterCard 7158300734726758'))
print(mask_account_card('Visa Classic 6831982476737658'))

# def get_data(my_date: str) -> str:
#     '''возвращает дату в виде ДД.ММ.ГГГГ'''
#     pass

