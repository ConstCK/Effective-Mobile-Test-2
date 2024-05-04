import datetime

import pytest
import jsonlines

from budget import Budget
from fake_db import *

my_test = Budget(name="John Doe", db_name="test.json", new=True)


def test_get_initial_data():
    """Тест Получения данных из пустой БД"""
    assert my_test.get_all_data() == [{"id": 0, "name": "John Doe",
                                       "balance": 0,
                                       "spending": 0,
                                       "income": 0}]


def test_get_initial_meta_data():
    """Тест Получения мета данных из пустой БД"""
    assert my_test.get_meta() == {"id": 0, "name": "John Doe",
                                  "balance": 0,
                                  "spending": 0,
                                  "income": 0}


@pytest.mark.parametrize("data, mode, expected", [(i_1, "Доходы", "Успешное добавление данных"),
                                                  (i_2, "Доходы", "Успешное добавление данных"),
                                                  (s_1, "Расходы", "Успешное добавление данных"),
                                                  (s_2, "Расходы", "Успешное добавление данных")
                                                  ])
def test_create_data(data, mode, expected):
    """Тест добавления информации в БД"""
    assert my_test.add_data(data, mode) == expected


def test_get_all_data():
    """Тест получения всех данных из БД"""
    assert my_test.get_all_data() == [
        {"id": 0, "name": "John Doe", "balance": 19000, "spending": 11000, "income": 30000},
        {"id": 1, "category": "Доходы", "date": str(datetime.date.today()), "price": i_1.get("price"),
         "description": i_1.get("description")},
        {"id": 2, "category": "Доходы", "date": str(datetime.date.today()), "price": i_2.get("price"),
         "description": i_2.get("description")},
        {"id": 3, "category": "Расходы", "date": str(datetime.date.today()), "price": s_1.get("price"),
         "description": s_1.get("description")},
        {"id": 4, "category": "Расходы", "date": str(datetime.date.today()), "price": s_2.get("price"),
         "description": s_2.get("description")}]


@pytest.mark.parametrize("mode, expected",
                         [("Доходы", [{"id": 1, "category": "Доходы", "date": str(datetime.date.today()),
                                       "price": i_1.get("price"), "description": i_1.get("description")},
                                      {"id": 2, "category": "Доходы", "date": str(datetime.date.today()),
                                       "price": i_2.get("price"), "description": i_2.get("description")}]),
                          ("Расходы", [{"id": 3, "category": "Расходы", "date": str(datetime.date.today()),
                                        "price": s_1.get("price"), "description": s_1.get("description")},
                                       {"id": 4, "category": "Расходы", "date": str(datetime.date.today()),
                                        "price": s_2.get("price"), "description": s_2.get("description")}])])
def test_get_by_category(mode, expected):
    """Тест получения данных по категории"""
    assert my_test.get_data_by_category(mode) == expected


@pytest.mark.parametrize("year, month, day, expected", [(str(datetime.date.today().year),
                                                         f"{datetime.date.today().month:02}",
                                                         f"{datetime.date.today().day:02}",
                                                         [{"id": 1, "category": "Доходы",
                                                           "date": str(datetime.date.today()),
                                                           "price": i_1.get("price"),
                                                           "description": i_1.get("description")},
                                                          {"id": 2, "category": "Доходы",
                                                           "date": str(datetime.date.today()),
                                                           "price": i_2.get("price"),
                                                           "description": i_2.get("description")},
                                                          {"id": 3, "category": "Расходы",
                                                           "date": str(datetime.date.today()),
                                                           "price": s_1.get("price"),
                                                           "description": s_1.get("description")},
                                                          {"id": 4, "category": "Расходы",
                                                           "date": str(datetime.date.today()),
                                                           "price": s_2.get("price"),
                                                           "description": s_2.get("description")}])])
def test_get_by_date(year, month, day, expected):
    """Тест получения данных по дате"""
    assert my_test.get_data_by_date(year, month, day) == expected


@pytest.mark.parametrize("price, expected", [(s_1.get("price"),
                                              [{"id": 3, "category": "Расходы", "date": str(datetime.date.today()),
                                                "price": s_1.get("price"), "description": s_1.get("description")}])])
def test_get_by_price(price, expected):
    """Тест получения данных по id"""
    assert my_test.get_data_by_sum(price) == expected


@pytest.mark.parametrize("data_id, data, expected", [(1, c_1, "Успешное изменение данных")])
def test_change_data(data_id, data, expected):
    """Тест изменение существующих данных"""
    assert my_test.change_data(data_id, data) == expected


def test_change_wrong_data():
    """Тест изменение несуществующих данных"""
    with pytest.raises(Exception):
        my_test.change_data(100, c_1)


def test_get_meta_data():
    """Тест Получения мета данных из БД"""
    assert my_test.get_meta() == {"id": 0,
                                  "name": "John Doe",
                                  "balance": 49000,
                                  "spending": 11000,
                                  "income": 60000}
