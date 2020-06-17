from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#chrome_options = webdriver.ChromeOptions()
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-extensions")


driver = Chrome(chrome_options=chrome_options, executable_path='../drivers/chromedriver')
driver.get('https://google.com')
print(driver.title)
driver.find_element(By.NAME,"q").send_keys('Automation step by step')
driver.find_element(By.NAME, "btnK").click()
print(driver.title)
driver.close()
driver.quit()
print('Completed')