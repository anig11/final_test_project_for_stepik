from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators, BasePageLocators, BasketPageLocators
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, TimeoutException
import math
import pytest
from selenium import webdriver

class BasketPage(BasePage):
    
    def basket_should_by_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.COUNT_ITEMS),"The elements are there, but they shouldn't be"
        
    def should_by_empty_message(self):
        assert self.is_not_element_present(*BasketPageLocators.COUNT_ITEMS),"The elements are there, but they shouldn't be"
        empty_message = self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY).text     
        assert "Your basket is empty." in empty_message,"No empty message "
            
            