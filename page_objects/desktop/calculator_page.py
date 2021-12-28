from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Calculator_Page:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_tow(self):
        return self.driver.find_element_by_name("Two")

    def get_seven(self):
        return self.driver.find_element_by_name("Seven")

    def get_clear(self):
        return self.driver.find_element_by_name("Clear")

    def get_equels(self):
        return self.driver.find_element_by_name("Equals")

    def get_multi(self):
        return self.driver.find_element_by_name("Multiply by")

    def get_result(self):
        return self.driver.find_elements_by_xpath("//*[@AutomationId='CalculatorResults']")

    def get_result(self):
        # trim extra text and whitespace off of the display value
        return self.driver.find_element_by_xpath("//*[@AutomationId='CalculatorResults']").text.replace("Display is",
                                                                                                        "").strip()
