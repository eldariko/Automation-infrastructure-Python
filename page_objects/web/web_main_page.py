from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class WebMainPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def tab_mine(self):
        return self.driver.find_element_by_xpath("//span[text()='Mine']")

    def txt_user_name(self):
        return self.driver.find_element_by_xpath("//h6[@data-test='sidenav-username']")

    def input_user_name(self):
        return self.driver.find_element_by_id("username")

    def input_password(self):
        return self.driver.find_element_by_id("password")

    def input_confirm_password(self):
        return self.driver.find_element_by_id("confirmPassword")

    def button_sign_up(self):
        return self.driver.find_element_by_xpath("//span[text()='Sign Up']")

    def txt_get_started(self):
        return By.XPATH, "//h2[text()='Get Started with Real World App']"

    def tab_bank_acoount(self):
        return By.XPATH, "//span[text()='Bank Accounts']"

    def tab_notifications(self):
        return By.XPATH, "//span[text()='Notifications']"

    def button_create(self):
        return By.XPATH, "//span[text()='Create']"

    def txt_bank_name(self, bank_name):
        return By.XPATH, f"//p[@class='MuiTypography-root MuiTypography-body1 MuiTypography-colorPrimary MuiTypography-gutterBottom'][text()='{bank_name}']"

    def button_new_transaction(self):
        return By.XPATH, "//span[text()=' New']"

    def button_contact_name(self, contact_name):
        return By.XPATH, f"//span[text()='{contact_name}']"

    def input_amount(self):
        return By.ID, "amount"

    def input_note(self):
        return By.ID, "transaction-create-description-input"

    def button_action(self, action):
        return By.XPATH, f"//span[text()='{action}']"

    def txt_account_balance(self):
        return By.XPATH, "//h6[@data-test='sidenav-user-balance']"
