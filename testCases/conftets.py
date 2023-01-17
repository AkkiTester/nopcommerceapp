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

#########pytest HTML##############
def pytest_configure(config):
    config._metadata['Project Name']='non Commerce'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester']='Akash'

@pytest.mark.optionhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)




