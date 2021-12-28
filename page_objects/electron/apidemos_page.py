from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Apidemos_Page:

    def __init__(self, driver: WebDriver):
        self.driver = driver
    def get_btn_windows(self):
        return self.driver.find_element_by_id("button-windows")

    def get_btn_crash(self):
        return self.driver.find_element_by_id("button-crash-hang")

    def get_btn_menuus(self):
        return self.driver.find_element_by_id("button-menus")

    def get_nav_itemes(self):
        return len(self.driver.find_elements_by_class_name("nav-item u-category"))

    def cust_me(self):
        return self.driver.find_element_by_xpath("// *[ @ id = 'menus-section'] / header / div / h1")


