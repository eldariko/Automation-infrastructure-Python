import allure
from selenium.webdriver.common.by import By


class MobileMainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("returns element enters TVM Calculator")
    def get_tvm_calc(self):
        return By.XPATH, "//*[@text='TVM Calculator']"

    @allure.step("returns element enters Currency Converter")
    def get_currency_converter(self):
        return By.XPATH, "//*[@text='Currency Converter']"

    @allure.step("returns element enters Loan Calculator")
    def get_loan_calc(self):
        return By.XPATH, "//*[@text='Loan Calculator']"

    @allure.step("returns element enters Compound Interest Calculator")
    def get_compound_interest_calc(self):
        return By.XPATH, "//*[@text='Compound Interest Calculator']"

    @allure.step("returns element enters Credit Card Payoff Calculator")
    def get_cc_payoff_calc(self):
        return By.XPATH, "//*[@text='Credit Card Payoff Calculator']"
