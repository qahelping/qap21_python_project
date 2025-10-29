from selenium.webdriver.common.by import By

url = "https://practice-automation.com/tables/"


def test_find_element(driver_firefox):
    driver_firefox.get(url)
    element = driver_firefox.find_element(By.CSS_SELECTOR, ".wp-block-heading")
    assert element.text == "Simple Table"


def test_find_elements(driver_firefox):
    driver_firefox.get(url)
    elements = driver_firefox.find_elements(By.CSS_SELECTOR, ".wp-block-heading")
    assert elements[0].text == "Simple Table", f"Expected text is {elements[0].text}"
    assert elements[1].text == "Sortable Table", f"Expected text is {elements[1].text}"


def test_get_attribute(driver_firefox):
    driver_firefox.get(url)
    element = driver_firefox.find_element(By.XPATH, "//section")
    assert element.get_attribute("class") == "title title-3 text-center    container-1400"


def test_get_attribute_disabled(driver_firefox):
    driver_firefox.get(url)
    element = driver_firefox.find_element(By.ID, "isDisabled")
    assert element.get_attribute("disabled")

    element = driver_firefox.find_element(By.ID, "color")
    assert not element.get_attribute("disabled")


def test_get_css(driver_firefox):
    driver_firefox.get(url)
    element = driver_firefox.find_element(By.XPATH, "//section")
    assert element.value_of_css_property("font-size") == "18px"


def test_get_tag_name(driver_firefox):
    driver_firefox.get(url)
    element = driver_firefox.find_element(By.ID, "isDisabled")
    assert element.tag_name == "button"

    element = driver_firefox.find_element(By.ID, "color")
    assert element.tag_name == "button"

    element = driver_firefox.find_element(By.CLASS_NAME, "card")
    assert element.tag_name == "div"
