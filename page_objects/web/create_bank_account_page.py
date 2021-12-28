from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class CreateBankAccountPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def locator_bank_name(self):
        return By.ID, "bankaccount-bankName-input"

    def locator_routing_number(self):
        return By.ID, "bankaccount-routingNumber-input"

    def locator_account_number(self):
        return By.ID, "bankaccount-accountNumber-input"

    def locator_button_save(self):
        return By.XPATH, "//span[text()='Save']"
