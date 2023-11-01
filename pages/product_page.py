from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math



class ProductPage(BasePage):
    
    def book_title_is_the_same(self):
        book_title_text = self.browser.find_element(*ProductPageLocators.Book_title).text
        book_title_in_basket = self.browser.find_element(*ProductPageLocators.Book_title_in_basket).text
        
        assert book_title_text == book_title_in_basket, "book title is wrong"
        
    def price_is_the_same(self):
        price_book = self.browser.find_element(*ProductPageLocators.Price_book).text
        price_book_in_basket = self.browser.find_element(*ProductPageLocators.Price_in_basket).text
        
        assert price_book == price_book_in_basket, "price is not same"
    
    def should_button_add_product_in_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.Add_Button)
        basket_button.click()
        
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
            
    def scroll_page(self):
        self.browser.execute_script("window.scrollBy(0, 200);")
        
        
    