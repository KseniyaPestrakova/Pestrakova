import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    filename="..\\logs\\masks.log",
    filemode="w",
)

masks_logger = logging.getLogger("masks")


def get_mask_card_number(card_number: str) -> str:
    """Возвращает маску номера карты в формате XXXX XX** **** XXXX"""

    masks_logger.info("Starting func get_mask_card_number")
    if len(str(card_number)) != 16:
        masks_logger.error(f"Wrong card_number {card_number}")
        raise ValueError("Номер карты должен состоять из 16 цифр")
    masks_logger.info(
        f'Successful return card_number using mask: {str(card_number)[:4] + " " + str(card_number)[4:6] + "** **** "
                                                     + str(card_number)[-4:]}'
    )
    return str(card_number)[:4] + " " + str(card_number)[4:6] + "** **** " + str(card_number)[-4:]


def get_mask_account(account_number: str) -> str:
    """Возвращает маску номера счета в формате **XXXX"""

    masks_logger.info("Starting func get_mask_account")
    if len(str(account_number)) != 20:
        masks_logger.error(f"Wrong account_number {account_number}")
        raise ValueError("Номер карты должен состоять из 16 цифр")
    masks_logger.info(f'Successful return account_number using mask: {"**" + str(account_number)[-4:]}')
    return "**" + str(account_number)[-4:]
