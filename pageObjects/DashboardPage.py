from selenium.webdriver.common.by import By

class DashboardPage():
    lnk_dashboard_xpath = "//p[@class='oxd-userdropdown-name']"
    lnk_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def clickDashboard(self):
        self.driver.find_element(By.XPATH,self.lnk_dashboard_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.lnk_logout_xpath).click()
