from selenium import webdriver
import pytest




    # driver.get("https://rahulshettyacademy.com/angularpractice/")
    # driver.maximize_window()

    ## cls => class => fixture attached class or a class which is using this fixture For now BaseClass
    ## adding attribute driver to BaseClass and assing value of driver we created here
    # request.cls.driver = driver         ## request => to class which is using fixture
    # yield
    # driver.close()
@pytest.fixture(scope="module")
def setup(request):
    browser=request.config.getoption("--browser")
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Firefox()
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

# @pytest.fixture()
# def browser(request):  # This will return the Browser value to setup method
#     return request.config.getoption("--browser")
#########pytest HTML##############
def pytest_configure(config):
    config._metadata['Project Name']='non Commerce'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester']='Akash'






