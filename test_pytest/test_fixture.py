import random

import pytest


@pytest.fixture(scope="module")
def lst():
    lst_temp = []
    for i in range(10):
        lst_temp.append(random.randint(0, 100))
    yield lst_temp
    print(lst_temp)


class TestFixture:

    def test_plus(self, fixture_function_autouse_false):
        print("Запустился тест")
        print("Значение фикстуры", "fixture_function_autouse_false")
        assert 1 + 2 == 2
        print("Тест окончен", "fixture_function_autouse_false")


# Создать 2 теста и фикстуру
# 1 - провяряет размер списка = 10
# 2 - проверяет что последний элемент = 0
# в фикстуре создается один список и заполняется рандомными данными, список должен быть один на 2 теста
def test_1(lst):
    assert 10 == len(lst)


def test_2(lst):
    assert lst[-1] == 0
