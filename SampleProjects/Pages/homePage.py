from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from SampleProjects.Locators.Locators import Locators


class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.welcome_menu_item_id = Locators.welcome_menu_item_id
        self.logout_menu_item_link_text = Locators.logout_menu_item_link_text

    def click_welcome(self):
        self.driver.find_element(By.ID, self.welcome_menu_item_id).click()

    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.logout_menu_item_link_text))).click()


