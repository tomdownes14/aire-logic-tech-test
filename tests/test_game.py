import os
import time
import unittest
from selenium import webdriver
from page_objects.home import HomePage
from page_objects.game import GamePage
from utils.data import get_random_string
from utils.driver import get_driver_for_browser


class CookieClickerGameTests(unittest.TestCase):
    def setUp(self):
        browser = os.getenv("BROWSER", "chrome")
        self.driver = get_driver_for_browser(browser)
        self.driver.get(HomePage.URL)
        player_name = "test-player" + get_random_string(10)
        HomePage(self.driver).create_game(player_name)

    def tearDown(self):
        self.driver.quit()

    def test_click_increases_cookie_count(self):
        game_page = GamePage(self.driver)
        for _ in range(5):
            game_page.click_cookie_button()
            time.sleep(0.1)

        self.assertEqual("5", game_page.get_number_of_cookies())

    def test_can_sell_cookies_for_money(self):
        game_page = GamePage(self.driver)
        game_page.buy_cookies(5)
        game_page.sell_cookies(5)

        self.assertEqual("0", game_page.get_number_of_cookies())
        self.assertEqual("5.0", game_page.get_number_of_money())

    def test_cannot_sell_cookies_player_does_not_own(self):
        game_page = GamePage(self.driver)
        game_page.sell_cookies(5)

        self.assertEqual("0.0", game_page.get_number_of_money())

    def test_cannot_sell_string_value_cookies(self):
        game_page = GamePage(self.driver)
        game_page.sell_cookies("cookies")

        self.assertEqual("0.0", game_page.get_number_of_money())

    def test_can_buy_factory_with_money(self):
        game_page = GamePage(self.driver)
        game_page.buy_cookies(5)
        game_page.sell_cookies(5)

        game_page.buy_factories(1)

        self.assertEqual("1", game_page.get_number_of_factories())
        self.assertEqual("2", game_page.get_number_of_money())

    def test_cannot_buy_factory_with_insufficient_money(self):
        game_page = GamePage(self.driver)
        game_page.buy_factories(1)

        self.assertEqual("0", game_page.get_number_of_factories())
        self.assertEqual("0.0", game_page.get_number_of_money())

    def test_cannot_buy_factory_string_value(self):
        game_page = GamePage(self.driver)
        game_page.buy_cookies(5)
        game_page.sell_cookies(5)

        game_page.buy_factories("cookie")

        self.assertEqual("0", game_page.get_number_of_factories())
        self.assertEqual("0.0", game_page.get_number_of_money())

    def test_factory_increases_cookies_without_clicking(self):
        game_page = GamePage(self.driver)
        game_page.buy_cookies(5)
        game_page.sell_cookies(5)

        cookies_before_factory = game_page.get_number_of_cookies()

        game_page.buy_factories(1)
        # wait for factory to produce cookies
        time.sleep(2)

        cookies_after_factory = game_page.get_number_of_cookies()

        self.assertGreater(cookies_after_factory, cookies_before_factory)
