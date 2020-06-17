import unittest
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))



from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from SampleProjects.Pages.loginPage import LoginPage
from SampleProjects.Pages.homePage import HomePage

class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()


    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_user_name('Admin')
        login.enter_password('admin123')
        login.click_login_button()

        home_page = HomePage(driver)
        home_page.click_welcome()
        home_page.click_logout()



        # self.driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
        # self.driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
        # self.driver.find_element(By.ID, 'btnLogin').click()f
        # self.driver.find_element(By.ID, 'welcome').click()
        # self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


print("Test Completed")

if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/vlad/python_projects/demo_test/SampleProjects/Reports'))