from selenium.webdriver.common.by import By

from element_example.core.base_element import BaseElement
from element_example.core.base_page import BasePage
from element_example.core.loctors_helper import get_contains_class


class LoginLocators(BasePage):

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
        self.DESCRIPTION = BaseElement(
            driver, (By.ID, get_contains_class("instrument-info__description"), "Description")
        )
        self.LOGO = ""
