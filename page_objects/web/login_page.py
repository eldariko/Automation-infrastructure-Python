from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LoginPage:
    locator_input_user_name = (By.ID, "username")
    locator_input_password = (By.ID, "password")
    locator_button_sign_in = (By.XPATH, "//span[text()='Sign In']")
    locator_link_sign_up = (By.XPATH, "//a[@href='/signup']")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def input_user_name(self):
        return self.driver.find_element(self.locator_input_user_name[0], self.locator_input_user_name[1])

    def input_password(self):
        return self.driver.find_element_by_id("password")

    def button_sign_in(self):
        return self.driver.find_element_by_xpath("//span[text()='Sign In']")

    def link_sign_up(self):
        return self.driver.find_element_by_xpath("//a[@href='/signup']")
