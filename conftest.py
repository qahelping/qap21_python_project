import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from files import BASE_DIR

pytest_plugins = [
    "fixtures.fixtures_pytest",
]


@pytest.fixture(scope="module", autouse=True)
def fixture_module_autouse_false():
    print("Фикстура МODULE fixture_class_autouse_false --- ")
    yield "----"
    print("Фикстура МODULE закончила действие fixture_class_autouse_false --- ")


def pytest_addoption(parser):
    parser.addoption("--br", action="store", default="chrome", help="the name of the browser")


@pytest.fixture(scope="function", autouse=False)
def driver(pytestconfig):
    browser = pytestconfig.getoption("--br")
    driver = None
    if browser == "chrome":
        options = ChromeOptions()
        options.add_experimental_option(
            "prefs",
            {
                "download.default_directory": str(BASE_DIR / "files"),  # Change default directory for downloads
                "download.prompt_for_download": False,  # To auto download the file
                "download.directory_upgrade": True,
                "plugins.always_open_pdf_externally": False,  # It will not show PDF directly in chrome
            },
        )
        options.add_argument("--window-size=1940,1600")
        options.headless = False

        driver = webdriver.Chrome(options=options)
    if browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--window-size=1640,900")
        options.headless = False

        driver = webdriver.Firefox(options=options)

    yield driver
    driver.quit()
