from selenium.webdriver.common.by import By

from element_example.core.base_element import BaseElement
from pageobject_example.pageobject.base_page import BasePage


class SuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.TITLE = BaseElement(driver, (By.CLASS_NAME, "post-title"))
        self.TEXT = BaseElement(driver, (By.TAG_NAME, "strong"))
        self.BUTTON_LOGOUT = BaseElement(driver, (By.CSS_SELECTOR, "a.wp-block-button__link"))

    def click_logout(self):
        self.BUTTON_LOGOUT.click()

        self.click(self.BUTTON_LOGOUT)

    def check_that_page_opened(self, title, text):
        self.TITLE.should_be_visible()
        self.TEXT.should_be_visible()
        self.BUTTON_LOGOUT.should_be_visible()

        self.TITLE.should_be_has_text(title)
        self.TEXT.should_be_has_text(text)

        self.should_be_visible(self.TITLE)
        self.should_be_visible(self.TEXT)
        self.should_be_visible(self.BUTTON_LOGOUT)

        self.should_be_has_text(self.TITLE, title)
        self.should_be_has_text(self.TEXT, text)
