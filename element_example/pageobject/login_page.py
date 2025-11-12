from selenium.webdriver.common.by import By

from element_example.core.base_element import BaseElement
from pageobject_example.pageobject.base_page import BasePage
from pageobject_example.urls import URLS


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.MENU_PRACTICE = BaseElement(driver, (By.CSS_SELECTOR, "#menu-item-20"))
        self.MENU_HOME = BaseElement(driver, (By.CSS_SELECTOR, "#menu-item-43"))
        self.MENU_COURSES = BaseElement(driver, (By.CSS_SELECTOR, "#menu-item-21"))
        self.MENU_BLOG = BaseElement(driver, (By.CSS_SELECTOR, "#menu-item-19"))
        self.MENU_CONTACT = BaseElement(driver, (By.CSS_SELECTOR, "#menu-item-18"))
        self.PAGE_TITLE = BaseElement(driver, (By.CSS_SELECTOR, "#login h2"))
        self.PAGE_DESCRIPTION = BaseElement(driver, (By.CSS_SELECTOR, "#login ul li:nth-child(1)"))
        self.PAGE_TEXT_INFO = BaseElement(driver, (By.XPATH, '//*[@id="login"]/ul/li[2]'))
        self.PAGE_TEXT_CREDS = BaseElement(driver, (By.CSS_SELECTOR, "#login > ul > li:nth-child(2) b"))
        self.INPUT_USER_NAME = BaseElement(driver, (By.ID, "username"))
        self.INPUT_PASSWORD = BaseElement(driver, (By.ID, "password"))
        self.SUBMIT = BaseElement(driver, (By.ID, "submit"))
        self.LINE = BaseElement(driver, (By.CLASS_NAME, ".wp-block-separator"))
        self.ERROR = BaseElement(driver, (By.ID, "error"))

    def open_page(self):
        self.open(URLS.BASE + URLS.LOGIN)

    def check_that_page_opened(self, title, description):
        self.MENU_COURSES.should_be_visible()

        self.should_be_visible(self.LOGO)
        self.should_be_visible(self.MENU_PRACTICE)
        self.should_be_visible(self.MENU_COURSES)
        self.should_be_visible(self.MENU_CONTACT)
        self.should_be_visible(self.MENU_BLOG)
        self.should_be_visible(self.PAGE_TEXT_CREDS)
        self.should_be_visible(self.SUBMIT)
        self.should_be_visible(self.INPUT_PASSWORD)
        self.should_be_visible(self.INPUT_USER_NAME)
        self.should_be_visible(self.PAGE_TITLE)
        self.should_be_visible(self.PAGE_DESCRIPTION)
        self.should_be_visible(self.PAGE_TEXT_INFO)

        self.should_be_has_text(self.PAGE_TITLE, title)
        self.should_be_has_text(self.PAGE_DESCRIPTION, description)

        self.should_be_not_visible(self.ERROR)

    def login(self, username, password):
        self.fill(self.INPUT_USER_NAME, text=username)
        self.fill(self.INPUT_PASSWORD, text=password)
        self.click(self.SUBMIT)
        return self

    def check_that_error_is_visible(self, text):
        self.should_be_visible(self.ERROR)
        self.should_be_has_text(self.ERROR, text)
        return self
