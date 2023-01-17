import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from testCases.conftets import setup

class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    def test_homePageTitle(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot('.\\Screenshots\\'+'test_homePageTitle.png')
            self.driver.close()
            assert False


    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_titel=self.driver.title
        if act_titel=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_login.png')
            self.driver.close()
            assert False
