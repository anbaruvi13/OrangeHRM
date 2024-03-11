import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os


class Test_Login:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_login(self, setup):
        self.logger.info("******* Starting test_001_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.targetpage = self.lp.isDashboardPageExists()
        if self.targetpage:
            assert True

        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login")
            assert False

        self.driver.close()
        self.logger.info("******* End of test_001_login **********")
