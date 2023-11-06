from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
import pytest
from selenium import webdriver

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        
    def scroll_page(self):
        self.browser.execute_script("window.scrollBy(0, 200);")
    
    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "The link is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),"Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM),"Register form is not presented"
        
    def register_new_user(self,email_new,password_new):
        email_input = self.browser.find_element(*LoginPageLocators.LOGIN_USER)
        email_input.send_keys(email_new)
        password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        password.send_keys(password_new)
        password2 = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD)
        password2.send_keys(password_new)
        button_registration = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        button_registration.click()