import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from mainObject import MainObject
from cartObject import CartObject
from productObject import ProductObject
from registrationObject import RegistrationObject

driver = webdriver.Chrome(service=ChromeService())
#################################1##################################
def screenshot():
    main_page = MainObject(driver)
    main_page.go()
    time.sleep(1)
    product_page = ProductObject(driver)
    time.sleep(1)
    product_page.open_product()
    time.sleep(1)
    product_page.image_click()
    time.sleep(1)
    product_page.next_image()
    time.sleep(1)
    product_page.next_image()
    time.sleep(1)

#################################2##################################

def cart():
    main_page = MainObject(driver)
    main_page.go()
    time.sleep(2)
    cart_page = CartObject(driver)
    time.sleep(1)
    cart_page.add_cart_button()
    time.sleep(1)
    buy_message = driver.find_element(By.CSS_SELECTOR, "body:nth-child(2) div.container:nth-child(4) > div.alert.alert-success.alert-dismissible")
    if "iPhone добавлен в корзину покупок!" in buy_message.text:
        print("Товар добавлен в корзину")
    time.sleep(1)

#################################3##################################

def category():
    main_page = MainObject(driver)
    main_page.go()
    time.sleep(1)
    main_page.open_pc_category()
    time.sleep(2)
    nothing_message = driver.find_element(By.CSS_SELECTOR, "body:nth-child(2) div.container:nth-child(4) div.row div.col-sm-9 > p:nth-child(2)")
    if "В данной категории нет товаров." in nothing_message.text:
        print("Проверка на категорию пройдена пройдена!")

#################################4##################################

def registration():
    main_page = MainObject(driver)
    main_page.go()
    time.sleep(2)
    register_page = RegistrationObject(driver)
    time.sleep(1)
    register_page.open_registration_page()
    time.sleep(1)
    register_page.registration_user("aaaaaa", "aaaaaa", "aaaaaa@gmail.com", "5214125", "aaAAaa@")
    time.sleep(1)

#################################5##################################

def main_input():
    main_page = MainObject(driver)
    main_page.go()
    time.sleep(2)
    main_page.search("Iphone")
    time.sleep(1)

#################################6##################################

def add_to_wishlist():
    main_page = MainObject(driver)
    main_page.go()
    time.sleep(1)
    product_page = ProductObject(driver)
    time.sleep(1)
    product_page.add_to_wishlist(2)
    time.sleep(1)

#################################7##################################

def add_camera():
    main_page = MainObject(driver)
    main_page.go()
    product_page = ProductObject(driver)
    time.sleep(1)
    product_page.add_cart_button(4)
    time.sleep(1)
    product_page.camera()
    time.sleep(1)

#################################8##################################

def add_clipboard():
    main_page = MainObject(driver)
    main_page.go()
    time.sleep(1)
    main_page.open_category("Планшеты")
    time.sleep(1)
    product_page = ProductObject(driver)
    time.sleep(1)
    product_page.add_to_cart_clipboard()
    time.sleep(1)

#################################9##################################

def add_htc():
    main_page = MainObject(driver)
    main_page.go()
    time.sleep(1)
    main_page.open_category("Телефоны")
    time.sleep(1)
    product_page = ProductObject(driver)
    time.sleep(1)
    product_page.add_to_cart_htc()
    time.sleep(2)

#################################10##################################

def submit_review():
    main_page = MainObject(driver)
    time.sleep(2)
    main_page.go()
    time.sleep(2)
    search_item = driver.find_element(By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child(2) div.product-thumb.transition div.image a:nth-child(1) > img.img-responsive")
    search_item.click()
    product_page = ProductObject(driver)
    time.sleep(1.5)
    product_page.open_review_form()
    time.sleep(1.5)
    product_page.submit_review("aaaaaaa", "ааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааа")
    time.sleep(1.5)


screenshot()
print("1 тест выполнен успешно!")
cart()
print("2 тест выполнен успешно!")
category()
print("3 тест выполнен успешно!")
registration()
print("4 тест выполнен успешно!")
main_input()
print("5 тест выполнен успешно!")
add_to_wishlist()
print("6 тест выполнен успешно!")
add_camera()
print("7 тест выполнен успешно!")
add_clipboard()
print("8 тест выполнен успешно!")
add_htc()
print("9 тест выполнен успешно!")
submit_review()
print("10 тест выполнен успешно!")