import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from testCases.conftets import setup
from utilities.customLogger import LogGen
from utilities import XLUtils


############AKK#############
class Test_002_DDT_Login:
    baseURL=ReadConfig.getApplicationURL()
    path='.//TestData/LoginData.xlsx'

    logger=LogGen.loggen()



    def test_login_ddt(self,setup):
        self.logger.info('************************* Test_002_DDT_Login *************************')
        self.logger.info("************************* Verifying Login DDT test *************************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print('Number of Row in a Excel:',self.rows)

        lst_ststus=[]

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title='Dashboard / nopCommerce administration'

            if act_title==exp_title:
                if self.exp=='Pass':
                    self.logger.info('****** Passed ******')
                    self.lp.clickLogout()
                    lst_ststus.append("pass")
                elif self.exp=="Fail":
                    self.logger.info('****** Failed *****')
                    self.lp.clickLogout()
                    lst_ststus.append("pass")
            elif act_title!=exp_title:
                if self.exp == 'Pass':
                    self.logger.info('****** Failed ******')
                    lst_ststus.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info('****** Passed *****')
                    lst_ststus.append("pass")

        if "Fail" not in lst_ststus:
            self.logger.info('********* Login DDT Test Is Passed *******')
            self.driver.close()
            assert True
        else:
            self.logger.info('********* Login DDT Test Is Failed *******')
            self.driver.close()
            assert False
        self.logger.info('********* End of Login DDT Test ***************')
        self.logger.info('********* Completed TC LoginDDT_002 ***************')
