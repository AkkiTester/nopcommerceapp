#pytest -v --html=repot.html --browser 'firefox'
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from testCases.conftets import setup
import testCases.conftets
from utilities.customLogger import LogGen


#@pytest.mark.usefixtures("setup")
class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()


    def test_homePageTitle(self,setup):
        self.logger.info("************************* Test_001_Login *************************")
        self.logger.info("************************* Verifying Home Page Title *************************")

        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            self.logger.info("************************* Home Page Title is passed *************************")
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot('.\\Screenshots\\'+'test_homePageTitle.png')
            self.driver.close()
            self.logger.error("************************* Home Page Title is failed *************************")
            assert False


    # def test_login(self,setup):
    #     self.logger.info("************************* Verifying Login test *************************")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.lp=LoginPage(self.driver)
    #     self.lp.setUserName(self.username)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogin()
    #     act_titel=self.driver.title
    #     if act_titel=="Dashboard / nopCommerce administration":
    #         self.logger.info("************************* Login test is passed *************************")
    #         assert True
    #         self.driver.close()
    #     else:
    #         self.driver.save_screenshot('.\\Screenshots\\' + 'test_login.png')
    #         self.driver.close()
    #         self.logger.error("************************* Login test is failed *************************")
    #         assert False
