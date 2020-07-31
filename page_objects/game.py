import time
from selenium.webdriver.common.by import By
from page_objects.base import BasePage


class GamePage(BasePage):
    WELCOME_MESSAGE = (By.CSS_SELECTOR, "body p")
    COOKIE_NUMBER = (By.ID, "cookies")
    MONEY_NUMBER = (By.ID, "money")
    FACTORY_NUMBER = (By.ID, "factories")
    COOKIE_BUTTON = (By.ID, "click")
    COOKIES_TO_SELL_INPUT = (By.ID, "cookies-to-sell")
    COOKIES_TO_SELL_BUTTON = (By.ID, "sell-cookies")
    FACTORIES_TO_BUY_INPUT = (By.ID, "factories-to-buy")
    FACTORIES_TO_BUY_BUTTON = (By.ID, "buy-factories")

    def __init__(self, driver):
        super().__init__(driver)

    def get_welcome_message(self):
        return self._get_element_text(self.WELCOME_MESSAGE)

    def click_cookie_button(self):
        self._click(self.COOKIE_BUTTON)

    def buy_cookies(self, cookies_to_buy):
        for _ in range(cookies_to_buy):
            self._click(self.COOKIE_BUTTON)
            time.sleep(0.1)

    def sell_cookies(self, cookies_to_sell):
        self._send_keys(self.COOKIES_TO_SELL_INPUT, cookies_to_sell)
        self._click(self.COOKIES_TO_SELL_BUTTON)

    def buy_factories(self, factories_to_buy):
        self._send_keys(self.FACTORIES_TO_BUY_INPUT, factories_to_buy)
        self._click(self.FACTORIES_TO_BUY_BUTTON)

    def get_number_of_cookies(self):
        return self._get_element_text(self.COOKIE_NUMBER)

    def get_number_of_money(self):
        return self._get_element_text(self.MONEY_NUMBER)

    def get_number_of_factories(self):
        return self._get_element_text(self.FACTORY_NUMBER)
