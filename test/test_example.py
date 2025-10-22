import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=640,900")
    driver = webdriver.Chrome(options=opts)
    yield driver

    driver.quit()


def test_selenium_web(driver):
    url = "https://www.selenium.dev/"
    driver.get(url)
    assert driver.title == "Selenium"
    assert driver.current_url == url


def test_pytest(driver):
    url = "https://docs.pytest.org/en/stable/"
    driver.get(url)
    assert driver.title == "pytest documentation"
    assert driver.current_url == url
