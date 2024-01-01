import os
from typing import List, Dict

from config import ROOT_DIR
from src.utils import (get_all_operations,get_executed_only,
                       get_sort_operations,hide_requisites,
                       get_formated_operations)

def test_get_all_operations():
    TEST_FAIL_PATH_1 = os.path.join(ROOT_DIR, 'tests', 'file_lkz_test.json' )
    assert get_all_operations(TEST_FAIL_PATH_1) == [1,2,3,4,5]
def test_get_executed_only():
    date_1 =  [{"id": "1", "date": "01.01.2023", "state": "EXECUTED"},
           {},
           {"id": "2", "date": "01.03.2023", "state": "EXECUTED"},
           {"id": "3", "date": "01.02.2023", "state": "EXECUTED"},
           {"id": "4", "date": "01.05.2023", "state": "CANCELED"},
           {"id": "5", "date": "01.04.2023", "state": "EXECUTED"},
           {"id": "6", "date": "01.06.2023", "state": "EXECUTED"}]
    result_1 =[{"id": "1", "date": "01.01.2023", "state": "EXECUTED"},
           {"id": "2", "date": "01.03.2023", "state": "EXECUTED"},
           {"id": "3", "date": "01.02.2023", "state": "EXECUTED"},
           {"id": "5", "date": "01.04.2023", "state": "EXECUTED"},
           {"id": "6", "date": "01.06.2023", "state": "EXECUTED"}]
    assert get_executed_only(date_1) == result_1
def test_get_sort_operations():
    date_2 = [{"id": "2", "date": "2020-05-19T12:51:49.023880", "state": "EXECUTED"},
           {"id": "3", "date": "2018-12-24T20:16:18.819037", "state": "EXECUTED"},
           {"id": "4", "date": "2017-06-20T03:59:34.851630", "state": "EXECUTED"},
           {"id": "5", "date": "2019-09-06T00:48:01.081967", "state": "EXECUTED"}]

    result_2 = [{"date":"2020-05-19T12:51:49.023880","id": "2", "state": "EXECUTED"},
           {"date":"2019-09-06T00:48:01.081967","id": "5", "state": "EXECUTED"},
           {"date":"2018-12-24T20:16:18.819037","id": "3", "state": "EXECUTED"},
           {"date":"2017-06-20T03:59:34.851630","id": "4", "state": "EXECUTED"}]
    assert get_sort_operations(date_2) == result_2
def test_hide_requisites():
    date_3_1 = ("Visa Gold 3654412434951162")
    date_3_2 = ("МИР 3766446452238784")
    date_3_3 = ("Счет 86655182730188443980")
    date_3_4 = ("Maestro 1308795367077170")
    result_3_1 = ("Visa Gold 3654 41 ** **** 1162")
    result_3_2 = ("МИР 3766 44 ** **** 8784")
    result_3_3 = ("Счет **3980")
    result_3_4 = ("Maestro 1308 79 ** **** 7170")
    assert hide_requisites(date_3_1) == result_3_1
    assert hide_requisites(date_3_2) == result_3_2
    assert hide_requisites(date_3_3) == result_3_3
    assert hide_requisites(date_3_4) == result_3_4

def test_get_formated_operations():
    date_4_1 = {'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
                 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
                 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}
    date_4_2 = {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890',
                 'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
                 'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012', 'to': 'Счет 35158586384610753655'}
    result_4_1 = "08.12.19 Открытие вклада\n"\
                 "Нет данных -->  Счет **5907\n"\
                 "41096.24 USD\n"
    result_4_2 = "07.12.19 Перевод организации\n"\
                 "Visa Classic 2842 87 ** **** 9012 -->  Счет **3655\n"\
                 "48150.39 USD\n"

    assert get_formated_operations(date_4_1) == result_4_1
    assert get_formated_operations(date_4_2) == result_4_2

