from selenium.webdriver.common.by import By

url = "https://letcode.in/test"


def test_form(driver_firefox):
    driver_firefox.get(url)
    element = driver_firefox.find_elements(By.CLASS_NAME, "card-footer-item")[18]
    element.click()

    assert driver_firefox.current_url == "https://letcode.in/forms"
    assert driver_firefox.title == "Forms | LetCode with Koushik"

    element = driver_firefox.find_element(By.ID, "firstname")
    element.send_keys("Alisa")

    element = driver_firefox.find_element(By.ID, "lasttname")
    element.send_keys("Selezneva")

    element = driver_firefox.find_element(By.ID, "email")
    assert element.is_displayed()
    element.clear()
    element.send_keys("AlisaSelezneva@gmail.com")

    element = driver_firefox.find_element(By.ID, "Phno")
    element.send_keys("11111111")

    element = driver_firefox.find_element(By.ID, "Addl1")
    element.send_keys("Addl1")

    element = driver_firefox.find_element(By.ID, "Addl2")
    element.send_keys("Addl12")

    element = driver_firefox.find_element(By.ID, "female")
    element.click()
    assert element.is_selected()

    element = driver_firefox.find_element(By.ID, "male")
    assert not element.is_selected()

    element = driver_firefox.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    element.click()
    assert element.is_selected()

    element = driver_firefox.find_element(By.CSS_SELECTOR, '[type="submit"]')
    element.submit()


def test_execute_script(driver_firefox):
    driver_firefox.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_button_test")
    driver_firefox.switch_to.frame("iframeResult")

    element = driver_firefox.find_element(By.CSS_SELECTOR, '[type="button"]')
    element.click()
    # driver_firefox.execute_script("arguments[0].click();", (By.CLASS_NAME, 'card-footer-item'))

    assert driver_firefox
