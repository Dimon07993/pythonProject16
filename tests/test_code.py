import pytest
import datetime
import json
from utils.code import sort_data, format_date, secret_card, load_file, print_data


def test_load_file(tmp_path):
    # Create a temporary file with some sample data
    test_data = {"key": "value"}
    file_path = tmp_path / "test_file.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(test_data, f)

    # Call the load_file function and check the result
    loaded_data = load_file(file_path)
    assert loaded_data == test_data


def test_sort_data():
    data = [
        {"state": "EXECUTED", "date": "2022-01-01T12:00:00.000"},
        {"state": "EXECUTED", "date": "2022-01-02T12:00:00.000"},
        {"state": "CANCELED", "date": "2022-01-03T12:00:00.000"},
    ]
    sorted_data = sort_data(data)
    assert len(sorted_data) == 2
    assert sorted_data[0]["date"] == "2022-01-01T12:00:00.000"
    assert sorted_data[1]["date"] == "2022-01-02T12:00:00.000"


def test_format_date():
    formatted_date = format_date("2022-01-01T12:00:00.000")
    assert formatted_date == "01.01.2022"


def test_secret_card():
    secret_check = secret_card("Счет 58518872592028002662")
    secret_map = secret_card('Visa Classic 5211277418228469')
    assert secret_map == "Visa Classic 5211 27** **** 8469"
    assert secret_check == "Счет **2662"


def test_print_data():
    assert print_data('tests\configtest.json') == [{'date': '30.06.2018', 'from': 'Счет **6952', 'to': 'Счет **6702',
                                              'operationAmount': {'amount': '9824.07',
                                                                  'currency': {'name': 'USD', 'code': 'USD'}},
                                              'descr': 'Перевод организации'}]
