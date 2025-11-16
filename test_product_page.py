import pytest
import time

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_catalogue_page()
    catalogue_page = ProductPage(browser, browser.current_url)
    catalogue_page.go_to_product_page()
    promo_url = browser.current_url + "?promo=newYear2019"
    product_page = ProductPage(browser, promo_url)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_able_add_product_to_basket()

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
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_able_add_product_to_basket()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_catalogue_page()
    catalogue_page = ProductPage(browser, browser.current_url)
    catalogue_page.go_to_product_page()
    promo_url = browser.current_url + "?promo=newYear2019"
    product_page = ProductPage(browser, promo_url)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_able_add_product_to_basket()
    product_page.should_not_be_success_message() 

def test_guest_cant_see_success_message(browser): 
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_catalogue_page()
    catalogue_page = ProductPage(browser, browser.current_url)
    catalogue_page.go_to_product_page()
    promo_url = browser.current_url + "?promo=newYear2019"
    product_page = ProductPage(browser, promo_url)
    product_page.open()
    product_page.should_not_be_success_message() 

def test_message_disappeared_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_catalogue_page()
    catalogue_page = ProductPage(browser, browser.current_url)
    catalogue_page.go_to_product_page()
    promo_url = browser.current_url + "?promo=newYear2019"
    product_page = ProductPage(browser, promo_url)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_able_add_product_to_basket()
    product_page.should_disappear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.xfail
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_catalogue_page()
    catalogue_page = ProductPage(browser, browser.current_url)
    catalogue_page.go_to_product_page()
    promo_url = browser.current_url + "?promo=newYear2019"
    product_page = ProductPage(browser, promo_url)
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_text()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser): 
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_catalogue_page()
        catalogue_page = ProductPage(browser, browser.current_url)
        catalogue_page.go_to_product_page()
        promo_url = browser.current_url + "?promo=newYear2019"
        product_page = ProductPage(browser, promo_url)
        product_page.open()
        product_page.should_not_be_success_message() 

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_catalogue_page()
        catalogue_page = ProductPage(browser, browser.current_url)
        catalogue_page.go_to_product_page()
        promo_url = browser.current_url + "?promo=newYear2019"
        product_page = ProductPage(browser, promo_url)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_able_add_product_to_basket()
