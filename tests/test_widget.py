from typing import Any

import pytest

from src.widget import get_data, mask_account_card


@pytest.fixture
def bad_number() -> Any:
    return 12345


@pytest.mark.parametrize(
    "client_info, expected",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ],
)
def test_mask_account_card(client_info: str, expected: str) -> None:
    assert mask_account_card(client_info) == expected


def test_mask_account_card_invalid_info(bad_number: Any) -> None:
    with pytest.raises(ValueError):
        mask_account_card(bad_number)


@pytest.mark.parametrize(
    "my_date, expected", [("2018-07-11T02:26:18.671407", "11.07.2018"), ("2024-06-29", "29.06.2024")]
)
def test_get_data(my_date: str, expected: str) -> None:
    assert get_data(my_date) == expected


def test_get_get_data_enough_str(bad_number: Any) -> None:
    with pytest.raises(ValueError):
        get_data(str(bad_number))
