def test_get_cookies(driver_firefox):
    url = "https://testpages.eviltester.com/styled/search"
    driver_firefox.get(url)
    cookies = driver_firefox.get_cookies()

    assert cookies


def test_get_cookie_seleniumSimplifiedSearchLastVisit(driver_firefox):
    url = "https://testpages.eviltester.com/styled/search"
    driver_firefox.get(url)
    cookie = driver_firefox.get_cookie("seleniumSimplifiedSearchLastVisit")

    assert cookie


def test_delete_cookie_seleniumSimplifiedSearchLastVisit(driver_firefox):
    url = "https://testpages.eviltester.com/styled/search"
    driver_firefox.get(url)
    driver_firefox.delete_cookie("seleniumSimplifiedSearchLastVisit")
    cookie = driver_firefox.get_cookie("seleniumSimplifiedSearchLastVisit")

    assert not cookie


def test_delete_all_cookies(driver_firefox):
    url = "https://testpages.eviltester.com/styled/search"
    driver_firefox.get(url)
    driver_firefox.delete_all_cookies()
    cookie = driver_firefox.get_cookie("seleniumSimplifiedSearchNumVisits")

    assert not cookie


def test_add_cookie(driver_firefox):
    url = "https://testpages.eviltester.com/styled/search"
    driver_firefox.get(url)
    driver_firefox.add_cookie({"name": "seleniumSimplifiedLastSearch", "value": "Selenium-RC"})

    driver_firefox.refresh()
    cookie = driver_firefox.get_cookie("seleniumSimplifiedLastSearch")

    assert cookie


def test_add_cookie_httbin(driver_firefox):
    url = "https://httpbin.org/"
    driver_firefox.get(url)
    driver_firefox.add_cookie(
        {"name": "seleniumSimplifiedLastSearch", "value": "Selenium-RC", "path": "/", "httpOnly": False}
    )
    driver_firefox.get("https://httpbin.org/cookies")

    assert driver_firefox.page_source
