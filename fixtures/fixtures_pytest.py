import pytest


@pytest.fixture(scope="class", autouse=True)
def fixture_class_autouse_false():
    print("Фикстура КЛАСС fixture_class_autouse_false --- ")
    yield "----"
    print("Фикстура КЛАСС закончила действие fixture_class_autouse_false --- ")


@pytest.fixture()
def fixture_function_autouse_false():
    print("Фикстура fixture_function_autouse_false --- ")
    yield "----"
    print("Фикстура закончила действие fixture_function_autouse_false --- ")


@pytest.fixture(scope="module", autouse=True)
def fixture_module_autouse_false():
    print("Фикстура МODULE fixture_class_autouse_false --- ")
    yield "----"
    print("Фикстура МODULE закончила действие fixture_class_autouse_false --- ")


@pytest.fixture(scope="session", autouse=True)
def fixture_session_autouse_false():
    print("Фикстура СЕССИЯ fixture_class_autouse_false --- ")
    yield "----"
    print("Фикстура СЕССИЯ закончила действие fixture_class_autouse_false --- ")
