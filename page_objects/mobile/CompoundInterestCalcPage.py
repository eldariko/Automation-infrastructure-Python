from selenium.webdriver.common.by import By


def get_principal_amount_edit_txt():
    return By.XPATH, "//*[@id='principleInput']"


def get_monthly_deposit_edit_txt():
    return By.XPATH, "//*[@id='monthlyDepositInput']"


def get_period_edit_txt():
    return By.XPATH, "//*[@id='periodInput']"


def get_annual_interest_rate_edit_txt():
    return By.XPATH, "//*[@id='interestRateInput']"


def get_calc_btn():
    return By.XPATH, "//*[@text='CALCULATE']"


def get_total_principal_txt_view():
    return By.XPATH, "//*[@id='totalPrincipalResult']"


def get_interest_amount_txt_view():
    return By.XPATH, "//*[@id='interestAmountResult']"


def get_maturity_value_txt_view():
    return By.XPATH, "//*[@id='totalResult']"


def get_apy_txt_view():
    return By.XPATH, "//*[@id='apyResult']"


def get_back_btn():
    return By.XPATH, "//*[@id='action_bar']/android.widget.ImageButton"
