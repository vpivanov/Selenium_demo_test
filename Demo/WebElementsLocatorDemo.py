from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://google.com")
driver.find_element(By.NAME, 'q').send_keys("Pivanov")
time.sleep(2)
driver.find_element(By.XPATH, "//div[@id='lga']").click()
driver.find_element(By.XPATH, "//div[@class='FPdoLc tfB0Bf']//input[@name='btnK']").click()