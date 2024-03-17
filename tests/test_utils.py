import pytest

from src import utils


def test_get_data():
    data = utils.get_data()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_data_for_main():
    with pytest.raises(FileNotFoundError):
        utils.get_data(True)


def test_get_last_operation(operations):
    data = utils.get_last_operations(operations, 1)

    assert data[0] == operations[0]


def test_format_date():
    assert utils.format_date("2018-09-12T21:27:25") == "12.09.2018"
    assert utils.format_date("2018-09-12T21:27:25.567") == "12.09.2018"


def test_format_dates():
    assert utils.format_account("Счет 90424923579946435907") == "Счет **5907"
    assert utils.format_account("Maestro 3928549031574026") == "Maestro 3928 54** **** 4026"
    assert utils.format_account("Visa Platinum 1246377376343588") == "Visa Platinum 1246 37** **** 3588"


def test_format_operation(operations):
    assert utils.format_operation(operations[0]) == "08.12.2019 Открытие вклада\nСчет **5907\n41096.24 USD"
    assert utils.format_operation(operations[1]) \
           == "12.09.2018 Перевод организации\nVisa Platinum 1246 37** **** 3588 -> Счет **1657\n67314.70 руб."


def test_format_operations(operations):
    assert utils.format_operations(operations) \
           == ("08.12.2019 Открытие вклада\nСчет **5907\n41096.24 USD\n\n"
               "12.09.2018 Перевод организации\nVisa Platinum 1246 37** **** 3588 -> Счет **1657\n67314.70 руб.")
