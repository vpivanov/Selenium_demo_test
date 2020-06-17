import unittest
import HtmlTestRunner

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_search_automation(self):
        self.driver.get("https://google.com")
        self.driver.find_element(By.NAME, 'q').send_keys("Automation")
        self.driver.find_element(By.NAME, 'btnK').click()
        print(self.driver.title)

    def test_search_automation_fail(self):
        self.driver.get("https://google.com")
        self.driver.find_element(By.NAME, 'q').send_keys("Automation")
        self.driver.find_element(By.NAME, 'btnK1').click()
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test compleated")

if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/vlad/python_projects/demo_test/reports'))
