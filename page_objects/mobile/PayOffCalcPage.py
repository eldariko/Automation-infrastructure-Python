from selenium.webdriver.common.by import By


def get_cc_balance_edit_txt():
    return By.XPATH, "//*[@id='balanceInput']"


def get_cc_interest_edit_txt():
    return By.XPATH, "//*[@id='interestInput']"


def get_payment_per_month_edit_txt():
    return By.XPATH, "//*[@id='paymentInput']"


def get_reset_btn():
    return By.XPATH, "//*[@text='RESET']"


def get_calc_btn():
    return By.XPATH, "//*[@text='CALCULATE']"


def get_result():
    return By.XPATH, "//*[@id='result']"


def get_back_btn():
    return By.XPATH, "//*[@contentDescription='Navigate up']"
