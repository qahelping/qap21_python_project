def test_open_site(selenium):
    selenium.get("https://www.google.com")
    assert "Google" in selenium.title


def test_test_click(selenium):
    selenium.get("https://www.google.com")
    element = selenium.find_element("xpath", "//a[contains(@href, '/kursy')]")
    element.click()
