from selenium.webdriver.common.by import By


def locator_bank_name():
    return By.ID, "bankaccount-bankName-input"


def locator_routing_number():
    return By.ID, "bankaccount-routingNumber-input"


def locator_account_number():
    return By.ID, "bankaccount-accountNumber-input"


def locator_button_save():
    return By.XPATH, "//span[text()='Save']"
