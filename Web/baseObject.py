from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseObject:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://demo-opencart.ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    def go(self):
        return self.driver.get(self.base_url)