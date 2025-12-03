import allure
import pytest

from pageobject_example.pageobject.login_page import LoginPage
from pageobject_example.pageobject.success_page import SuccessPage


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def success_page(driver):
    return SuccessPage(driver)


@pytest.fixture()
def open_page(login_page):
    login_page.open_page()


@pytest.mark.only
def test_check_all_elements(login_page, open_page):
    login_page.check_that_page_opened(
        title="Test login",
        description="This is a simple Login page. "
        "Students can use this page to practice writing simple positive and negative LogIn tests. "
        "Login functionality is something that most of the test automation engineers need to automate.",
    )


@pytest.mark.smoke
@allure.title("Authentication")
def test_positive_login(login_page, success_page, open_page):
    login_page.login("student", "Password123")
    success_page.check_that_page_opened(
        "Logged In Successfully", "Congratulations student. You successfully logged in!"
    )


@allure.title("Authentication 2")
@pytest.mark.smoke
def test_logout(login_page, success_page, open_page):
    login_page.login("student", "Password123")
    success_page.check_that_page_opened(
        "Logged In Successfully", "Congratulations student. You successfully logged in!"
    )
    success_page.click_logout()

    login_page.check_that_page_opened(
        title="Test login",
        description="This is a simple Login page. "
        "Students can use this page to practice writing simple positive and negative LogIn tests. "
        "Login functionality is something that most of the test automation engineers need to automate.",
    )


@pytest.mark.parametrize(
    "user, password, expect",
    [
        ("incorrectUser", "Password123", "Your username is invalid!"),
        ("student", "incorrectPassword", "Your password is invalid!"),
    ],
)
@pytest.mark.smoke
@allure.title("Authentication negative")
def test_negative_username(login_page, open_page, user, password, expect):
    login_page.login(user, password)
    login_page.check_that_error_is_visible(expect)
