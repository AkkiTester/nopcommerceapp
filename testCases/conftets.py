from selenium import webdriver
import pytest



def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )

@pytest.fixture()
def setup(request):
    browser=request.config.getoption('--browser')
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("lanching chrome browser......")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("lanching firefox browser......")
    else:
        driver=webdriver.Chrome()
    return driver






