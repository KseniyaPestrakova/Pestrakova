import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def bad_number() -> int:
    return 12345


@pytest.mark.parametrize(
    "card_number, expected", [(7000792289606361, "7000 79** **** 6361"), (7000792289605555, "7000 79** **** 5555")]
)
def test_get_mask_card_number(card_number: int, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_invalid_len(bad_number: int) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(bad_number)


@pytest.mark.parametrize(
    "account_number, expected", [(73654108430135874305, "**4305"), (73654108430135871234, "**1234")]
)
def test_get_mask_account(account_number: int, expected: str) -> None:
    assert get_mask_account(account_number) == expected


def test_get_mask_account_invalid_len(bad_number: int) -> None:
    with pytest.raises(ValueError):
        get_mask_account(bad_number)
