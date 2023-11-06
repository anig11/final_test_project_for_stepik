from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest
import random
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException,TimeoutException 

@pytest.mark.skip  
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.skip 
def test_guest_can_add_product_to_basket(browser,link):
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
    
@pytest.mark.skip    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.should_button_add_product_in_basket()
    page.should_not_be_success_message()

@pytest.mark.skip 
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()
    
@pytest.mark.skip 
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.should_button_add_product_in_basket()
    page.should_dissapear_of_success_message()    

@pytest.mark.skip    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.skip    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(5)
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_by_empty()
    basket_page.should_by_empty_message()


@pytest.mark.registation
class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page =  LoginPage(browser, link)
        page.open()
        email_new = str(time.time()) + "@fakemail.org"
        count = random.randint(1, 100)
        password_new = str(time.time() + count)
        page.scroll_page()
        page.register_new_user(email_new,password_new)
        page.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
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
    
    