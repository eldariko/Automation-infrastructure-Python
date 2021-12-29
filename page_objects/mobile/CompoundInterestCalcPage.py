from selenium.webdriver.common.by import By


class CompoundInterestCalcPage:
    def __init__(self, driver):
        self.driver = driver

    def get_principal_amount_edit_txt(self):
        return By.XPATH, "//*[@id='principleInput']"

    def get_monthly_deposit_edit_txt(self):
        return By.XPATH, "//*[@id='monthlyDepositInput']"

    def get_period_edit_txt(self):
        return By.XPATH, "//*[@id='periodInput']"

    def get_annual_interest_rate_edit_txt(self):
        return By.XPATH, "//*[@id='interestRateInput']"

    def get_calc_btn(self):
        return By.XPATH, "//*[@text='CALCULATE']"

    def get_total_principal_txt_view(self):
        return By.XPATH, "//*[@id='totalPrincipalResult']"

    def get_interest_amount_txt_view(self):
        return By.XPATH, "//*[@id='interestAmountResult']"

    def get_maturity_value_txt_view(self):
        return By.XPATH, "//*[@id='totalResult']"

    def get_apy_txt_view(self):
        return By.XPATH, "//*[@id='apyResult']"

    def get_back_btn(self):
        return By.XPATH, "//*[@contentDescription='Navigate up']"
