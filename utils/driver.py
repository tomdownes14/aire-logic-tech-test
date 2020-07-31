from selenium import webdriver


def get_driver_for_browser(browser):
    if browser.lower() == "chrome":
        return webdriver.Chrome("driver_binaries/chromedriver.exe")
    elif browser.lower() == "firefox":
        return webdriver.Firefox(executable_path="driver_binaries/geckodriver.exe")
