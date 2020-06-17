from selenium.webdriver.common.by import By
from POMDemo.Locators.locators import Locators


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_xpath = Locators.username_textbox_xpath
        self.password_textbox_xpath = "//input[@id='txtPassword']"
        self.login_button_xpath = "//input[@id='btnLogin']"

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, Locators.password_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, Locators.password_textbox_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

