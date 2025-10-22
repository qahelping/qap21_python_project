from selenium.webdriver.chrome.options import Options
import pytest
import time

from selenium import webdriver
@pytest.fixture
def driver():
    opts = Options(); opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    yield driver

    driver.quit()
def test_selenium_web(driver):
  url = "https://www.selenium.dev/https://www.selenium.dev/https://www.selenium.dev/https://www.selenium.dev/https://www.selenium.dev/https://www.selenium.dev/https://www.selenium.dev/https://www.selenium.dev/https://www.selenium.dev/"
  driver.get(url)
  assert driver.title == "Selenium1"
  assert driver.current_url == url




