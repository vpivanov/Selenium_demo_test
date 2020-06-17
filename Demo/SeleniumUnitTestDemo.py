import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("https://google.com")
        self.driver.find_element(By.NAME, 'q').send_keys("Automation Step by Step")
        self.driver.find_element(By.NAME, 'btnK').click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, 'Automation Step by Step - Google Search')

    def test_search_2(self):
        self.driver.get("https://google.com")
        self.driver.find_element(By.NAME, 'q').send_keys("Pivanov Vladimir")
        self.driver.find_element(By.NAME, 'btnK').click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, 'Pivanov Vladimir - Google Search')


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
