from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url):
        self.driver.get(url)

    def page_should_be_opened(self, expected_url, title=None):
        assert self.wait.until(EC.url_contains(expected_url))

        if title:
            assert self.wait.until(EC.title_contains(title))
