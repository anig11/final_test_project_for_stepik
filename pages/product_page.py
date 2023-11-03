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
        
    
    def scroll_page(self):
        self.browser.execute_script("window.scrollBy(0, 200);")
        
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is presented, but should not be"
        
    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is not disappeared"
        