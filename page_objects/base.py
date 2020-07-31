class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _click(self, selector):
        self.driver.find_element(*selector).click()

    def _send_keys(self, selector, value):
        self.driver.find_element(*selector).send_keys(value)

    def _find(self, selector):
        return self.driver.find_element(*selector)

    def _find_all(self, selector):
        return self.driver.find_elements(*selector)

    def _get_element_text(self, selector):
        return self.driver.find_element(*selector).text
