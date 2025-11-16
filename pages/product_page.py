from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def go_to_product_page(self):
        product_link = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE)
        product_link.click()

    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_able_add_product_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_name_in_the_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_THE_BASKET)
        product_price_in_the_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_THE_BASKET)

        assert product_name.text == product_name_in_the_basket.text, f"Название товара в алерте: '{product_name.text}' не совпадает с названием товара, добавленного в корзину: '{product_name_in_the_basket.text}'"
        assert product_price.text == product_price_in_the_basket.text, f"Цена товара в алерте: '{product_price.text}' не совпадает с ценой товара, добавленного в корзину: '{product_price_in_the_basket.text}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should disappear"
