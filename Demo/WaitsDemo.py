from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.implicitly_wait(10)

driver.get("https://google.com")
driver.find_element(By.NAME, 'q').send_keys("Automation")

wait = WebDriverWait(driver, 10)
try:
    elememt = wait.until(EC.element_to_be_clickable((By.NAME, 'btnK1')))
    print("element is clickable")
except:
    print("element is not clickable")
    exit(1)
elememt.click()
#driver.find_element(By.NAME, 'btnK').click()

print("Test Completed")
driver.close()
driver.quit()
