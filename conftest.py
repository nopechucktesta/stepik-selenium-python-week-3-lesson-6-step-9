import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default=None, help="Browser language")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    browser_options = Options()
    browser_options.add_experimental_option("prefs", {"intl.accept_languages": browser_language})
    browser = webdriver.Chrome(options=browser_options)
    yield browser
    browser.quit()
