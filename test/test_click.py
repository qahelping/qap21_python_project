import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    opts = ChromeOptions()
    opts.headless = True
    opts.add_argument("--window-size=640,900")
    driver = webdriver.Chrome(options=opts)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def open_site(driver, url="https://teachmeskills.by"):
    driver.get(url)


def click(driver, type_selector, selector):
    element = driver.find_element(type_selector, selector)
    element.click()


def assert_url(driver, expected_url):
    assert expected_url in driver.current_url, f"❌ Ошибка: ожидалось {expected_url}, но получили {driver.current_url}"


# 1. Обычный клик
def test_click(driver):
    open_site(driver)
    click(driver, By.XPATH, "//a[contains(@href, '/kursy')]")
    time.sleep(2)
    assert_url(driver, "kursy")
