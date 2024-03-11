from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    txt_username_xpath = "//input[@placeholder='Username']"
    txt_password_xpath = "//input[@placeholder='Password']"
    btn_login_xpath = "//button[normalize-space()='Login']"
    msg_dashboard_xpath = "//h6[normalize-space()='Dashboard']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def setUsername(self, username):
        self.driver.find_element(By.XPATH, self.txt_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def isDashboardPageExists(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.msg_dashboard_xpath)))
        except Exception as e:
            print(e)
        sleep(0.5)
        element = self.driver.find_element((By.XPATH, self.msg_dashboard_xpath))
        return element.is_displayed
