from selenium.webdriver.common.by import By

url = "https://letcode.in/frame"


def test_navigation(driver_firefox):
    driver_firefox.get(url)
    driver_firefox.find_element(By.ID, "multi").click()
    window_handles = driver_firefox.window_handles
    assert len(window_handles) == 3

    driver_firefox.switch_to.window(window_handles[1])
    current_url = driver_firefox.current_url
    assert current_url != url


def test_frame(driver_firefox):
    driver_firefox.get(url)
    frame = driver_firefox.find_element(By.ID, "firstFr")
    driver_firefox.switch_to.frame(frame)
    driver_firefox.find_element(By.CSS_SELECTOR, '[name="fname"]').send_keys("Artem")

    driver_firefox.switch_to.default_content()


def test_back_forward_button(driver_firefox):
    url = "http://zero.webappsecurity.com/"
    driver_firefox.get(url)
    driver_firefox.find_element(By.ID, "online-banking").click()
    current_url = driver_firefox.current_url
    assert url != current_url
    driver_firefox.back()
    assert url == driver_firefox.current_url
    assert current_url != driver_firefox.current_url

    driver_firefox.forward()
    assert url != driver_firefox.current_url
