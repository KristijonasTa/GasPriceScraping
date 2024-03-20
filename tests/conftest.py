import pytest
from selenium import webdriver
from utils.test_data import TestData
driver = None


@pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_driver(request):
    global driver
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(chrome_options)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()
    request.cls.driver = driver
    print("Browser: ", request.param)
    driver.get(TestData.url_base)
    driver.maximize_window()
    yield
    print("Close Driver")
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--email", action="store", default=TestData.gmail_recipients, help="Specify the email address")


@pytest.fixture
def email(request):
    return request.config.getoption("--email")
