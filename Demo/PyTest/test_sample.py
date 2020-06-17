import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSample():
    @pytest.fixture()
    def test_set_up(self):
        global driver
        driver = webdriver.Firefox(executable_path='C:/WebDriver/bin/geckodriver.exe')
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print('Test completed')


    def test_login(self, test_set_up):
        driver.get('https://opensource-demo.orangehrmlive.com/')
        driver.find_element(By.ID, 'txtUsername').send_keys("Admin")
        driver.find_element(By.ID, 'txtPassword').send_keys("admin123")
        driver.find_element(By.ID, 'btnLogin').click()
        x = driver.title
        assert x == "OrangeHRM"

    # def test_tear_down():
    #     driver.close()
    #     driver.quit()
    #     print('Test completed')

