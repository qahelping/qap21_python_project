url = "https://arty.name/localstorage.html"


def test_add_local_storage(driver_firefox):
    driver_firefox.get(url)
    driver_firefox.execute_script('window.localStorage.setItem("user", "Dima")')


def test_get_local_storage(driver_firefox):
    driver_firefox.get(url)
    local_storage = driver_firefox.execute_script('return window.localStorage.getItem("user")')

    assert local_storage


def test_get_all_local_storage(driver_firefox):
    driver_firefox.get(url)
    driver_firefox.execute_script("return Object.keys(window.localStorage);")

    assert driver_firefox


def test_delete_all_local_storage(driver_firefox):
    driver_firefox.get(url)
    driver_firefox.execute_script('window.localStorage.removeItem("name");')
