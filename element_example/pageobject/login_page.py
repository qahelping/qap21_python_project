from element_example.locators.login_locators import LoginLocators
from pageobject_example.pageobject.base_page import BasePage
from pageobject_example.urls import URLS


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginLocators(driver)

    def open_page(self):
        self.locators.open(URLS.BASE + URLS.LOGIN)

    def check_that_page_opened(self, title, description):
        self.locators.MENU_COURSES.should_be_visible()

        self.should_be_visible(self.locators.LOGO)
        self.should_be_visible(self.locators.MENU_PRACTICE)
        self.should_be_visible(self.locators.MENU_COURSES)
        self.should_be_visible(self.locators.MENU_CONTACT)
        self.should_be_visible(self.locators.MENU_BLOG)
        self.should_be_visible(self.locators.PAGE_TEXT_CREDS)
        self.should_be_visible(self.locators.SUBMIT)
        self.should_be_visible(self.locators.INPUT_PASSWORD)
        self.should_be_visible(self.locators.INPUT_USER_NAME)
        self.should_be_visible(self.locators.PAGE_TITLE)
        self.should_be_visible(self.locators.PAGE_DESCRIPTION)
        self.should_be_visible(self.locators.PAGE_TEXT_INFO)

        self.should_be_has_text(self.locators.PAGE_TITLE, title)
        self.should_be_has_text(self.locators.PAGE_DESCRIPTION, description)

        self.should_be_not_visible(self.locators.ERROR)

    def login(self, username, password):
        self.fill(self.locators.INPUT_USER_NAME, text=username)
        self.fill(self.locators.INPUT_PASSWORD, text=password)
        self.click(self.locators.SUBMIT)
        return self

    def check_that_error_is_visible(self, text):
        self.should_be_visible(self.locators.ERROR)
        self.should_be_has_text(self.locators.ERROR, text)
        return self
