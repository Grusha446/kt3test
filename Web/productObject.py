import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from baseObject import BaseObject

class ProductObject(BaseObject):
    PRODUCT_CLICK = (By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child(2) div.product-thumb.transition div.image a:nth-child(1) > img.img-responsive")
    IMAGE_CLICK = (By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(1) div.col-sm-8 ul.thumbnails li:nth-child(1) a.thumbnail > img:nth-child(1)")
    NEXT = (By.CSS_SELECTOR, " body:nth-child(2) div.mfp-wrap.mfp-gallery.mfp-close-btn-in.mfp-auto-cursor.mfp-ready:nth-child(2) div.mfp-container.mfp-s-ready.mfp-image-holder > button.mfp-arrow.mfp-arrow-right.mfp-prevent-close:nth-child(4)")

    def open_product(self):
        product_name = self.find_element(self.PRODUCT_CLICK)
        product_name.click()

    def image_click(self):
        thumbnail = self.find_elements(self.IMAGE_CLICK)[0]
        thumbnail.click()

    def next_image(self):
        next_button = self.find_element(self.NEXT)
        next_button.click()

    def add_cart_button(self, product_number):
        cart_button = self.find_element((By.CSS_SELECTOR, f"div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child("f"4) "f"div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child("f"{product_number}) div.product-thumb.transition div.button-group > "f"button:nth-child(1)"))
        cart_button.click()

    def camera(self):
        camera_option = self.find_element((By.ID, "input-option226"))
        camera_option.click()
        camera_option.send_keys(Keys.ARROW_DOWN)
        add_cart_button = self.find_element((By.ID, "button-cart"))
        add_cart_button.click()

    def add_to_cart_clipboard(self):
        add_cart_button = self.find_element((By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-9 div.row:nth-child(3) div.product-layout.product-grid.col-lg-4.col-md-4.col-sm-6.col-xs-12 div.product-thumb div:nth-child(2) div.button-group > button:nth-child(1)"))
        add_cart_button.click()

    def add_to_cart_htc(self):
        add_cart_button = self.find_element((By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-9 div.row:nth-child(3) div.product-layout.product-grid.col-lg-4.col-md-4.col-sm-6.col-xs-12:nth-child(1) div.product-thumb div:nth-child(2) div.button-group > button:nth-child(1)"))
        add_cart_button.click()

    def add_to_wishlist(self, product_number):
        add_to_wishlist_button = self.find_element((By.CSS_SELECTOR, f"div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child({product_number}) div.product-thumb.transition div.button-group button:nth-child(2) > i.fa.fa-heart"))
        add_to_wishlist_button.click()

    def open_review_form(self):
        review_link = self.find_element((By.XPATH, "//a[contains(text(),'Отзывов (0)')]"))
        review_link.click()

    def submit_review(self, name, review_text):
        name_input = self.find_element((By.ID, "input-name"))
        time.sleep(1.5)
        name_input.send_keys(name)
        time.sleep(1)
        review_input = self.find_element((By.ID, "input-review"))
        time.sleep(1.5)
        review_input.send_keys(review_text)
        time.sleep(1)
        rating_input = self.find_element((By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(1) div.col-sm-8 div.tab-content div.tab-pane.active:nth-child(2) form.form-horizontal div.form-group.required:nth-child(5) div.col-sm-12 > input:nth-child(6)"))
        rating_input.click()
        time.sleep(1)
        submit_button = self.find_element((By.ID, "button-review"))
        time.sleep(1.5)
        submit_button.click()

