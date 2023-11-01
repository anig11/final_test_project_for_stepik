from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

from selenium.common.exceptions import NoAlertPresentException



def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser,link)
    page.open()
    time.sleep(2)
    page.scroll_page()
    time.sleep(2)
    page.should_button_add_product_in_basket()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.scroll_page()
    time.sleep(2)
    page.book_title_is_the_same()
    time.sleep(2)
    page.price_is_the_same()
    
    
    