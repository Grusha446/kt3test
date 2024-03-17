from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from baseObject import BaseObject


class MainObject(BaseObject):
    def open_category(self, category_name):
        category_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//a[contains(text(),'{category_name}')]"))
        )
        category_link.click()

    def search(self, search_query):
        search_input = self.find_element((By.CSS_SELECTOR, "div.input-group > input.form-control.input-lg"))
        search_input.send_keys(search_query)
        search_button = self.find_element((By.CSS_SELECTOR, "div.input-group span.input-group-btn > button.btn.btn-default.btn-lg"))
        search_button.click()

    PC_CATEGORY = (By.CSS_SELECTOR, "div.container:nth-child(3) nav.navbar div.collapse.navbar-collapse.navbar-ex1-collapse ul.nav.navbar-nav li.dropdown:nth-child(1) > a.dropdown-toggle")
    PC_ITEM = (By.CSS_SELECTOR, "div.container:nth-child(3) nav.navbar div.collapse.navbar-collapse.navbar-ex1-collapse ul.nav.navbar-nav li.dropdown:nth-child(1) div.dropdown-menu div.dropdown-inner ul.list-unstyled li:nth-child(1) > a:nth-child(1)")
    PRODUCT_ITEMS = (By.CSS_SELECTOR, "div.container:nth-child(3) nav.navbar div.collapse.navbar-collapse.navbar-ex1-collapse ul.nav.navbar-nav li.dropdown:nth-child(1) div.dropdown-menu div.dropdown-inner ul.list-unstyled li:nth-child(1) > a:nth-child(1)")

    def open_pc_category(self):
        pc_category_link = self.find_element(self.PC_CATEGORY)
        pc_category_link.click()
        pc_category_item = self.find_element(self.PC_ITEM)
        pc_category_item.click()
