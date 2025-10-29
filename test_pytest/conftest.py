import pytest


@pytest.fixture(scope="package", autouse=True)
def fixture_package_autouse_false():
    print("Фикстура PACKEGE fixture_class_autouse_false --- ")
    yield "----"
    print("Фикстура PACKEGE закончила действие fixture_class_autouse_false --- ")
