import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url):
        self.driver.get(url)

    def get_element(self, selector, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(selector))
        return element

    def click(self, selector):
        element = self.get_element(selector)
        element.click()

    def fill(self, selector, text):
        element = self.get_element(
            selector,
        )
        element.send_keys(text)

    def page_should_be_opened(self, expected_url, title=None):
        assert self.wait.until(EC.url_contains(expected_url))

        if title:
            assert self.wait.until(EC.title_contains(title))

    @allure.step("should_be_has_text {selector}, {expected}")
    def should_be_has_text(self, selector, expected):
        with allure.step(f"Should be visible selector: {selector}" f"Expected text: {expected}"):

            element = self.get_element(selector)
            actual = element.text.strip()
            assert actual == expected, f"ACTUAL IS:  {actual}, EXPECTED IS: {expected}"

    def should_be_visible(self, selector):
        with allure.step(f"Should be visible selector: {selector}"):
            element = self.get_element(selector)
            assert element.is_displayed()

    @allure.step("Assert element is not visible")
    def should_be_not_visible(self, selector, timeout=5):
        element = WebDriverWait(self.driver, timeout).until_not(EC.element_to_be_clickable(selector))
        return element
