import pytest
from cases import case_login
from pytest_cases import parametrize_with_cases

user_types_ex = ["admin", "guest"]
browsers_ex = ["Chrome", "Firefox", "Safari"]
oses_ex = ["Windows", "macOS", "Linux"]


@pytest.mark.timeout(1)
@parametrize_with_cases("user_type, browser, os", cases=case_login)
def test_login_allpairs(user_type, browser, os):
    print(user_type, browser, os)


@pytest.mark.dependency()
def test_create_user():
    assert True


@pytest.mark.dependency(depends=["test_create_user"])
def test_delete_user():
    assert True
