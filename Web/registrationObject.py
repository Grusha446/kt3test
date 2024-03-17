import time
from selenium.webdriver.common.by import By
from baseObject import BaseObject

class RegistrationObject(BaseObject):
    MY_ACCOUNT = (By.CSS_SELECTOR, "div.container div.nav.pull-right ul.list-inline li.dropdown:nth-child(2) > a.dropdown-toggle")
    REGISTRATION = (By.CSS_SELECTOR, "div.container div.nav.pull-right ul.list-inline li.dropdown.open:nth-child(2) ul.dropdown-menu.dropdown-menu-right li:nth-child(1) > a:nth-child(1)")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#input-email")
    TELEPHONE_INPUT = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-confirm")
    PRIVACY_POLICY_AGREE = (By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-9 form.form-horizontal:nth-child(3) div.buttons:nth-child(4) div.pull-right > input:nth-child(3)")
    AGREE_BUTTON = (By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-9 form.form-horizontal:nth-child(3) div.buttons:nth-child(4) div.pull-right > input.btn.btn-primary:nth-child(4)")

    def open_registration_page(self):
        my_account = self.find_element(self.MY_ACCOUNT)
        my_account.click()
        registration = self.find_element(self.REGISTRATION)
        registration.click()

    def registration_user(self, first_name, last_name, email, telephone, password):
        first_name_input = self.find_element(self.FIRST_NAME_INPUT)
        first_name_input.send_keys(first_name)
        time.sleep(0.5)
        last_name_input = self.find_element(self.LAST_NAME_INPUT)
        last_name_input.send_keys(last_name)
        time.sleep(0.5)
        email_input = self.find_element(self.EMAIL_INPUT)
        email_input.send_keys(email)
        time.sleep(0.5)
        telephone_input = self.find_element(self.TELEPHONE_INPUT)
        telephone_input.send_keys(telephone)
        time.sleep(0.5)
        password_input = self.find_element(self.PASSWORD_INPUT)
        password_input.send_keys(password)
        time.sleep(0.5)
        confirm_password_input = self.find_element(self.CONFIRM_PASSWORD_INPUT)
        confirm_password_input.send_keys(password)
        time.sleep(0.5)
        privacy_policy_checkbox = self.find_element(self.PRIVACY_POLICY_AGREE)
        privacy_policy_checkbox.click()
        time.sleep(0.5)
        continue_button = self.find_element(self.AGREE_BUTTON)
        continue_button.click()
        time.sleep(0.5)