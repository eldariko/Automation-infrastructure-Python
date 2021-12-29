import allure
from selenium.webdriver.common.by import By


@allure.step("returns element enters TVM Calculator")
def get_tvm_calc():
    return By.XPATH, "//*[@text='TVM Calculator']"


@allure.step("returns element enters Currency Converter")
def get_currency_converter():
    return By.XPATH, "//*[@text='Currency Converter']"


@allure.step("returns element enters Loan Calculator")
def get_loan_calc():
    return By.XPATH, "//*[@text='Loan Calculator']"


@allure.step("returns element enters Compound Interest Calculator")
def get_compound_interest_calc():
    return By.XPATH, "//*[@text='Compound Interest Calculator']"


@allure.step("returns element enters Credit Card Payoff Calculator")
def get_cc_payoff_calc():
    return By.XPATH, "//*[@text='Credit Card Payoff Calculator']"
