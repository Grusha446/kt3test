import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=ChromeService())
################1###############
def screenshot():

    driver.get("https://demo-opencart.ru/index.php")

    seacrch_icon = driver.find_element(By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child(2) div.product-thumb.transition div.image a:nth-child(1) > img.img-responsive")
    seacrch_icon.click()
    time.sleep(1)
    driver.get("https://demo-opencart.ru/index.php?route=product/product&product_id=40")

    seacrch_image = driver.find_element(By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(1) div.col-sm-8 ul.thumbnails li:nth-child(1) a.thumbnail > img:nth-child(1)")
    seacrch_image.click()
    time.sleep(1)

    image_click = driver.find_element(By.CSS_SELECTOR, "body:nth-child(2) div.mfp-wrap.mfp-gallery.mfp-close-btn-in.mfp-auto-cursor.mfp-ready:nth-child(2) div.mfp-container.mfp-image-holder.mfp-s-ready > button.mfp-arrow.mfp-arrow-right.mfp-prevent-close:nth-child(4)")
    image_click.click()
    next_image = driver.find_element(By.CSS_SELECTOR, "div.mfp-wrap.mfp-gallery.mfp-close-btn-in.mfp-auto-cursor.mfp-ready:nth-child(2) div.mfp-container.mfp-image-holder.mfp-s-ready div.mfp-content:nth-child(1) div.mfp-figure figure:nth-child(2) > img.mfp-img:nth-child(1)")
    if seacrch_image != next_image:
        seacrch_cross = driver.find_element(By.CSS_SELECTOR, "div.mfp-wrap.mfp-gallery.mfp-close-btn-in.mfp-auto-cursor.mfp-ready:nth-child(2) div.mfp-container.mfp-image-holder.mfp-s-ready div.mfp-content:nth-child(1) div.mfp-figure > button.mfp-close:nth-child(1)")
        time.sleep(1)
        seacrch_cross.click()
        print("Картинка изменилась")
    time.sleep(1)

######################2#####################
def basket():
    driver.get("https://demo-opencart.ru/index.php?route=product/product&product_id=40")
    buy_button = driver.find_element(By.CSS_SELECTOR, "#button-cart")
    buy_button.click()
    time.sleep(1)
    buy_message = driver.find_element(By.CSS_SELECTOR, "body:nth-child(2) div.container:nth-child(4) > div.alert.alert-success.alert-dismissible")
    if "iPhone добавлен в корзину покупок!" in buy_message.text:
        print("Товар добавлен в корзину")
        cart_button = driver.find_element(By.CSS_SELECTOR, "#cart-total")
        cart_button.click()
        in_cart = driver.find_element(By.CSS_SELECTOR, "div.container div.row div.col-sm-3 div.btn-group.btn-block.open ul.dropdown-menu.pull-right li:nth-child(2) div:nth-child(1) p.text-right a:nth-child(1) > strong:nth-child(1)")
        in_cart.click()
        driver.get("https://demo-opencart.ru/index.php?route=checkout/cart")
        cross_button_cart = driver.find_element(By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.table-responsive table.table.table-bordered tr:nth-child(1) td.text-left:nth-child(4) div.input-group.btn-block span.input-group-btn > button.btn.btn-danger:nth-child(2)")
        cross_button_cart.click()
    time.sleep(1)

##################3###################
def category():
    driver.get("https://demo-opencart.ru/index.php?route=checkout/cart")
    category_button = driver.find_element(By.CSS_SELECTOR, "div.container:nth-child(3) nav.navbar div.collapse.navbar-collapse.navbar-ex1-collapse ul.nav.navbar-nav li.dropdown:nth-child(1) > a.dropdown-toggle")
    category_button.click()
    category_button_choose = driver.find_element(By.CSS_SELECTOR, "div.container:nth-child(3) nav.navbar div.collapse.navbar-collapse.navbar-ex1-collapse ul.nav.navbar-nav li.dropdown:nth-child(1) div.dropdown-menu div.dropdown-inner ul.list-unstyled li:nth-child(1) > a:nth-child(1)")
    category_button_choose.click()
    time.sleep(1)
    driver.get("https://demo-opencart.ru/index.php?route=product/category&path=20_26")
    nothing_message = driver.find_element(By.CSS_SELECTOR, "body:nth-child(2) div.container:nth-child(4) div.row div.col-sm-9 > p:nth-child(2)")
    if "В данной категории нет товаров." in nothing_message.text:
        print("Проверка на категорию пройдена пройдена!")
    time.sleep(1)
###################4##################

def registration():
    driver.get("https://demo-opencart.ru/index.php?route=product/category&path=20_26")
    user_button = driver.find_element(By.CSS_SELECTOR, "div.container div.nav.pull-right ul.list-inline li.dropdown:nth-child(2) a.dropdown-toggle > i.fa.fa-user")
    user_button.click()
    register_button = driver.find_element(By.CSS_SELECTOR, "div.container div.nav.pull-right ul.list-inline li.dropdown.open:nth-child(2) ul.dropdown-menu.dropdown-menu-right li:nth-child(1) > a:nth-child(1)")
    register_button.click()
    time.sleep(2)
    driver.get("https://demo-opencart.ru/index.php?route=account/register")
    time.sleep(1)
    search_firstname = driver.find_element(By.CSS_SELECTOR, "#input-firstname")
    letters = "aaaaaa"
    search_firstname.click()
    for letter in letters:
        search_firstname.send_keys(letter)
    time.sleep(1)
    search_lastname = driver.find_element(By.CSS_SELECTOR, "#input-lastname")
    letters = "aaaaaa"
    search_lastname.click()
    for letter in letters:
        search_lastname.send_keys(letter)
    time.sleep(1)
    search_email = driver.find_element(By.CSS_SELECTOR, "#input-email")
    letters = "aaaaaa@gmail.com"
    search_email.click()
    for letter in letters:
        search_email.send_keys(letter)
    time.sleep(1)
    search_phone = driver.find_element(By.CSS_SELECTOR, "#input-telephone")
    letters = "5214125"
    search_phone.click()
    for letter in letters:
        search_phone.send_keys(letter)
    time.sleep(1)
    search_password = driver.find_element(By.CSS_SELECTOR, "#input-password")
    letters = "aaAAaa@"
    search_password.click()
    for letter in letters:
        search_password.send_keys(letter)
    time.sleep(1)
    search_confirm_password = driver.find_element(By.CSS_SELECTOR, "#input-confirm")
    letters = "aaAAaa@"
    search_confirm_password.click()
    for letter in letters:
        search_confirm_password.send_keys(letter)
    time.sleep(1)
    search_agree = driver.find_element(By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-9 form.form-horizontal:nth-child(3) div.buttons:nth-child(4) div.pull-right > input:nth-child(3)")
    search_agree.click()
    search_confirm_registration = driver.find_element(By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-9 form.form-horizontal:nth-child(3) div.buttons:nth-child(4) div.pull-right > input.btn.btn-primary:nth-child(4)")
    search_confirm_registration.click()
    search_main_button = driver.find_element(By.CSS_SELECTOR, "div.container div.row div.col-sm-4 div:nth-child(1) h1:nth-child(1) > a:nth-child(1)")
    search_main_button.click()
    time.sleep(5)

##########5##################
def main_input():
    driver.get("https://demo-opencart.ru/index.php?route=common/home")
    search_input = driver.find_element(By.CSS_SELECTOR, "div.container div.row div.col-sm-5 div.input-group > input.form-control.input-lg")
    search_input.send_keys("Iphone")
    input_confirm = driver.find_element(By.CSS_SELECTOR, "div.container div.row div.col-sm-5 div.input-group span.input-group-btn button.btn.btn-default.btn-lg > i.fa.fa-search")
    input_confirm.click()
    time.sleep(5)

screenshot()
basket()
category()
registration()
main_input()