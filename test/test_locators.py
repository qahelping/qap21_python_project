import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# url = "https://letcode.in/test"
url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/register"


class EcommerceLocators:
    # Personal Details Section
    INPUT_FIRST_NAME = (By.XPATH, '//*[@name="firstname"]')
    INPUT_LAST_NAME = (By.CSS_SELECTOR, '[name="lastname"]')
    INPUT_EMAIL = (By.ID, "input-email")
    INPUT_TELEPHONE = (By.ID, "input-telephone")
    HINT_TELEPHONE = (By.ID, "input-telephone-help")

    # Password Section
    INPUT_PASSWORD = (By.ID, "input-password")
    INPUT_CONFIRM_PASSWORD = (By.ID, "input-confirm")

    # Newsletter Section
    RADIOBUTTON_SUBSCRIBE_YES = (By.ID, "input-newsletter-yes")
    RADIOBUTTON_SUBSCRIBE_NO = (By.ID, "input-newsletter-no")

    # Agreement and Submit Section
    CHECKBOX_AGREE = (By.ID, "input-agree")
    BUTTON_CONTINUE = (By.CSS_SELECTOR, 'input[type="submit"][value="Continue"]')
    PRIVACY_POLICY_LINK = (By.CSS_SELECTOR, 'a[href*="information/information/agree"]')

    # Customer Group (hidden by default)
    CUSTOMER_GROUP_DEFAULT = (By.CSS_SELECTOR, 'input[name="customer_group_id"][value="1"]')

    # Fieldset sections for verification
    FIELDSET_PERSONAL_DETAILS = (By.CSS_SELECTOR, "fieldset#account")
    FIELDSET_PASSWORD = (By.XPATH, '//fieldset[legend[contains(text(), "Your Password")]]')
    FIELDSET_NEWSLETTER = (By.XPATH, '//fieldset[legend[contains(text(), "Newsletter")]]')


def test_locators_selenium(driver):
    driver.get(url)
    # el = driver.find_elements(By.ID, "account-register")
    el = driver.find_elements(By.NAME, "search")[-1]
    el.send_keys("hello")

    el = driver.find_element(By.PARTIAL_LINK_TEXT, "login")
    el = driver.find_element(By.LINK_TEXT, "login")
    el.click()

    el = driver.find_element(By.TAG_NAME, "header")
    el.click()

    el = driver.find_elements(By.CLASS_NAME, "entry-section container")
    el.click()


def test_locators_css(driver):
    driver.get(url)
    el = driver.find_element(By.CSS_SELECTOR, ".my.test.class")
    el = driver.find_element(By.CSS_SELECTOR, "[class='my test class']")
    el = driver.find_element(By.CSS_SELECTOR, "p.class")

    el = driver.find_elements(By.CSS_SELECTOR, "[class='my test']")  # только один элемент
    el = driver.find_element(By.CSS_SELECTOR, "#firstName")
    el = driver.find_element(By.CSS_SELECTOR, "[id='firstName']")
    el = driver.find_element(By.CSS_SELECTOR, "input#firstName")
    el = driver.find_element(By.CSS_SELECTOR, "input#firstName")

    el = driver.find_element(By.CSS_SELECTOR, "article")
    el = driver.find_element(By.CSS_SELECTOR, '[href="https://www.facebook.com/HYRTutorials/"]')

    el = driver.find_element(By.CSS_SELECTOR, 'input[value="Confirm"]')

    el = driver.find_element(By.CSS_SELECTOR, 'div.widget[id="HTML910"]')

    el = driver.find_elements(By.CSS_SELECTOR, "form div p")[1]

    el = driver.find_element(By.CSS_SELECTOR, "form div p.contact-form-error-message")  # потомок любого уровня
    el = driver.find_element(By.CSS_SELECTOR, "form > div > p")  # прямой потомок

    el = driver.find_elements(By.CSS_SELECTOR, "div ~ a")  # сразу после

    el = driver.find_elements(By.CSS_SELECTOR, '[class^="ns-i1n0"]')  # начинается с
    el = driver.find_elements(By.CSS_SELECTOR, '[class$="e-5"]')  # заканчиваются
    el = driver.find_elements(By.CSS_SELECTOR, '[class*="tact-form"]')  # содержит

    el = driver.find_elements(By.CSS_SELECTOR, "div:first-child")  # первый потомок
    el = driver.find_elements(By.CSS_SELECTOR, "ul li:last-child")  # последний потомок
    el = driver.find_elements(By.CSS_SELECTOR, "ul li:last-child")  # последний потомок
    el = driver.find_elements(By.CSS_SELECTOR, "ul li:nth-child(3)")  # значение по номеру

    el = driver.find_elements(By.CSS_SELECTOR, 'div[class="top-bar-menu"] ul li:not([itemprop="name"])')
    el = driver.find_elements(By.CSS_SELECTOR, '[type="checkbox"]:checked')  # выбранный чекбокс
    el = driver.find_elements(By.CSS_SELECTOR, '[name="test"]:disabled')  # неактивный
    el = driver.find_elements(By.CSS_SELECTOR, '[name="test"]:enabled')  # активный

    el = driver.find_elements(By.CSS_SELECTOR, 'br ~ input.selectors-input[type="email"]')  # комби
    el = driver.find_element(
        By.CSS_SELECTOR, "li.menu-item.menu-item-type-custom.menu-item-object-custom.menu-item-21643 > a"
    )  # комби
    assert el.is_displayed()


def test_locators_xpath(driver):
    driver.get(url)
    el = driver.find_element(By.CSS_SELECTOR, '//*[@class="tm-menu"]')
    el = driver.find_element(By.CSS_SELECTOR, '//div[@class="tm-menu"]')
    el = driver.find_element(By.CSS_SELECTOR, '//*[@trbidi="on"]')

    el = driver.find_elements(By.CSS_SELECTOR, '//*[@id="main-wrapper"]')
    el = driver.find_element(By.CSS_SELECTOR, '//*[text()="Click below to confirm"]')  # text
    el = driver.find_element(By.CSS_SELECTOR, '//*[contains(@placeholder, "Enter your security")]')  #
    el = driver.find_element(By.CSS_SELECTOR, '//*[contains(@placeholder, "Enter your security")]')  #
    el = driver.find_element(By.CSS_SELECTOR, "[id='firstName']")
    el = driver.find_element(By.CSS_SELECTOR, "input#firstName")
    el = driver.find_element(By.CSS_SELECTOR, "input#firstName")

    el = driver.find_element(By.CSS_SELECTOR, "article")
    el = driver.find_element(By.CSS_SELECTOR, '[href="https://www.facebook.com/HYRTutorials/"]')

    el = driver.find_element(By.CSS_SELECTOR, 'input[value="Confirm"]')

    el = driver.find_element(By.CSS_SELECTOR, 'div.widget[id="HTML910"]')

    el = driver.find_elements(By.CSS_SELECTOR, "form div p")[1]

    el = driver.find_element(By.CSS_SELECTOR, "form div p.contact-form-error-message")  # потомок любого уровня
    el = driver.find_element(By.CSS_SELECTOR, "form > div > p")  # прямой потомок

    el = driver.find_elements(By.CSS_SELECTOR, "div ~ a")  # сразу после

    el = driver.find_elements(By.CSS_SELECTOR, '[class^="ns-i1n0"]')  # начинается с
    el = driver.find_elements(By.CSS_SELECTOR, '[class$="e-5"]')  # заканчиваются
    el = driver.find_elements(By.CSS_SELECTOR, '[class*="tact-form"]')  # содержит

    el = driver.find_elements(By.CSS_SELECTOR, "div:first-child")  # первый потомок
    el = driver.find_elements(By.CSS_SELECTOR, "ul li:last-child")  # последний потомок
    el = driver.find_elements(By.CSS_SELECTOR, "ul li:last-child")  # последний потомок
    el = driver.find_elements(By.CSS_SELECTOR, "ul li:nth-child(3)")  # значение по номеру

    el = driver.find_elements(
        By.CSS_SELECTOR, 'div[class="top-bar-menu"] ul li:not([itemprop="name"])'
    )  # значение по номеру
    el = driver.find_elements(By.CSS_SELECTOR, '[type="checkbox"]:checked')  # выбранный чекбокс
    el = driver.find_elements(By.CSS_SELECTOR, '[name="test"]:disabled')  # неактивный
    el = driver.find_elements(By.CSS_SELECTOR, '[name="test"]:enabled')  # активный

    el = driver.find_elements(By.CSS_SELECTOR, 'br ~ input.selectors-input[type="email"]')  # комби
    el = driver.find_elements(
        By.CSS_SELECTOR, "li.menu-item.menu-item-type-custom.menu-item-object-custom.menu-item-21643 > a"
    )  # комби
    assert el.is_displayed()


url = "https://www.wildberries.by/"


def test_locators():
    driver = webdriver.Chrome()
    driver.get(url)
    # el = driver.find_elements(By.ID, "account-register")
    el = driver.find_element(By.ID, "searchInput")  # поиск
    el.send_keys("hello")
    time.sleep(3)

    # el = driver.find_element(By.NAME, "banner_46a051b8-7e0a-4d7c-a75b-18b77f2c6cd3") #баннер
    # el.click()

    # меню полоски
    el = driver.find_element(By.CLASS_NAME, "header__bottom")
    el.click()
    time.sleep(3)

    el = driver.find_elements(By.CLASS_NAME, "j-item-basket")[0]
    el.click()

    time.sleep(3)
