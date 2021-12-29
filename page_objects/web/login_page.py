from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def input_user_name():
    return By.ID, "username"


def input_password():
    return By.ID, "password"


def button_sign_in():
    return By.XPATH, "//span[text()='Sign In']"


def link_sign_up():
    return By.XPATH, "//a[@href='/signup']"
