from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class NotificationsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def button_dismis(self):
        return By.XPATH, "//span[text()='Dismiss']"
