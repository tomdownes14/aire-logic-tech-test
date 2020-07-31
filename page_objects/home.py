from selenium.webdriver.common.by import By
from page_objects.base import BasePage
from page_objects.game import GamePage


class HomePage(BasePage):
    URL = "http://35.176.178.218:8888/"

    HEADING = (By.TAG_NAME, "h1")
    PLAYER_NAME_INPUT = (By.NAME, "name")
    START_GAME_BUTTON = (By.CSS_SELECTOR, "form button")
    CURRENT_GAME_LINKS = (By.CSS_SELECTOR, "tr td:first-child a")

    def __init__(self, driver):
        super().__init__(driver)

    def select_player_game(self, player_name):
        player_selector = (By.LINK_TEXT, player_name)
        self._click(player_selector)
        return GamePage(self.driver)

    def get_current_player_games(self):
        game_links = self._find_all(self.CURRENT_GAME_LINKS)
        return [link.text for link in game_links]

    def create_game(self, player_name):
        self._send_keys(self.PLAYER_NAME_INPUT, player_name)
        self._click(self.START_GAME_BUTTON)
        return GamePage(self.driver)
