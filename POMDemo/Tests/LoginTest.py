import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..", ".."))
import HtmlTestRunner

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from POMDemo.Pages.HomePage import HomePage
from POMDemo.Pages.loginPage import LoginPage




class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(5)

    def test_login_valid(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()

        home_page = HomePage(driver)
        home_page.click_welcome()
        home_page.click_logout()

        # self.driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys("Admin")
        # self.driver.find_element(By.XPATH, "//input[@id='txtPassword']").send_keys("admin123")
        # self.driver.find_element(By.XPATH, "//input[@id='btnLogin']").click()
        # self.driver.find_element(By.ID, 'welcome').click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/vlad/python_projects/demo_test/reports'))



