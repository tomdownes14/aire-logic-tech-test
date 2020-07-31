import os
import unittest
from page_objects.home import HomePage
from utils.driver import get_driver_for_browser
from utils.data import get_random_string


class CookieClickerHomeTests(unittest.TestCase):
    def setUp(self):
        browser = os.getenv("BROWSER", "chrome")
        self.driver = get_driver_for_browser(browser)
        self.driver.get(HomePage.URL)

    def tearDown(self):
        self.driver.quit()

    def test_create_new_game(self):
        player_name = "test-player" + get_random_string(10)

        home_page = HomePage(self.driver)
        game_page = home_page.create_game(player_name)

        self.assertIn(player_name, game_page.get_welcome_message())

    def test_access_saved_game(self):
        player_name = "test-player" + get_random_string(10)
        home_page = HomePage(self.driver)
        home_page.create_game(player_name)
        self.driver.get(HomePage.URL)

        self.assertIn(player_name, home_page.get_current_player_games())

        game_page = home_page.select_player_game(player_name)

        self.assertIn(player_name, game_page.get_welcome_message())

    def test_cannot_access_other_players_saved_game(self):
        player_name = "test-player" + get_random_string(10)
        home_page = HomePage(self.driver)
        home_page.create_game(player_name)
        self.driver.get(HomePage.URL)

        all_player_games = home_page.get_current_player_games()

        self.assertIn(player_name, all_player_games)
        self.assertEqual(1, len(all_player_games))
