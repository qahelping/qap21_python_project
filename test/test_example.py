def test_selenium_web(driver_firefox):
    url = "https://www.selenium.dev/"
    driver_firefox.get(url)
    assert driver_firefox.title == "Selenium"
    assert driver_firefox.current_url == url


def test_pytest(driver):
    url = "https://docs.pytest.org/en/stable/"
    driver.get(url)
    assert driver.title == "pytest documentation"
    assert driver.current_url == url
