import allure
import pytest
from _pytest.fixtures import FixtureRequest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    # iphone_11 = playwright.devices["iPhone 11 Pro"]
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
    }


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_bdd_after_scenario(request: FixtureRequest, feature, scenario):
    yield
    page = request.getfixturevalue("page")
    screenshot = page.screenshot()
    allure.attach(
        screenshot,
        name=f"Final screenshot - {scenario.name}",
        attachment_type=allure.attachment_type.PNG,
    )
