import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

pytest_plugins = [
    "fixtures.fixtures_pytest",
]


@pytest.fixture(scope="module", autouse=True)
def fixture_module_autouse_false():
    print("Фикстура МODULE fixture_class_autouse_false --- ")
    yield "----"
    print("Фикстура МODULE закончила действие fixture_class_autouse_false --- ")


@pytest.fixture
def driver():
    opts = ChromeOptions()
    opts.headless = True
    opts.add_argument("--window-size=640,900")
    driver = webdriver.Chrome(options=opts)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="function", autouse=False)
def driver_firefox():
    options = FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver

    driver.quit()
