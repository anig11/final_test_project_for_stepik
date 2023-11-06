from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR,"#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR,"#register_form")
    LOGIN_USER = (By.CSS_SELECTOR,"div.form-group > div #id_registration-email")
    LOGIN_PASSWORD = (By.CSS_SELECTOR,"div.form-group > div #id_registration-password1")
    REPEAT_PASSWORD = (By.CSS_SELECTOR,"div.form-group > div #id_registration-password2")
    BUTTON_REGISTRATION = (By.NAME,"registration_submit")

class ProductPageLocators():
    Add_Button = (By.CLASS_NAME,"btn.btn-lg.btn-primary.btn-add-to-basket")
    Book_title = (By.CSS_SELECTOR,"div.col-sm-6.product_main > h1")
    Book_title_in_basket = (By.CSS_SELECTOR,"div.alertinner > strong")
    Price_book = (By.CSS_SELECTOR,"div.col-sm-6.product_main > p.price_color")
    Price_in_basket = (By.CSS_SELECTOR,"div.alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR,"span.btn-group > a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():
    COUNT_ITEMS = (By.ID,"id_form-TOTAL_FORMS")
    MESSAGE_BASKET_IS_EMPTY =(By.CSS_SELECTOR,"#content_inner > p")
    
    
    