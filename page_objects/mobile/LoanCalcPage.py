from selenium.webdriver.common.by import By


class LoanCalcPage:
    def __init__(self, driver):
        self.driver = driver

    def get_amount_edit_txt(self):
        return self.driver.find_element(By.XPATH, "//*[@id='loanAmount']")

    def get_interest_rate_edit_txt(self):
        return self.driver.find_element(By.XPATH, "//*[@id='interestRate']")

    def get_loan_term_years_edit_txt(self):
        return self.driver.find_element(By.XPATH, "//*[@id='loanYear']")

    def get_loan_term_months_edit_txt(self):
        return self.driver.find_element(By.XPATH, "//*[@id='loanMonth']")

    def get_extra_payment_per_month_edit_txt(self):
        return self.driver.find_element(By.XPATH, "//*[@id='extraPerMonth']")

    def get_calc_btn(self):
        return self.driver.find_element(By.XPATH, "//*[@text='CALCULATE']")

    def get_monthly_payment_txt_view(self):
        return self.driver.find_element(By.XPATH, "//*[@text='2,040.23']")

    def get_total_payment_txt_view(self):
        return self.driver.find_element(By.XPATH, "//*[@text='30,576.41']")

    def get_total_interest_txt_view(self):
        return self.driver.find_element(By.XPATH, "//*[@text='576.41']")

    def get_annual_payment_txt_view(self):
        return self.driver.find_element(By.XPATH, "//*[@text='24,482.76']")

    def get_mortgage_constant_txt_view(self):
        return self.driver.find_element(By.XPATH, "//*[@text='81.61%']")

    def get_interest_saving_txt_view(self):
        return self.driver.find_element(By.XPATH, "//*[@text='27.04']")

    def get_payoff_earlier_txt_view(self):
        return self.driver.find_element(By.XPATH, "//*[@text='0 month']")

    def get_back_btn(self):
        return self.driver.find_element(By.XPATH, "//*[@contentDescription='Navigate up']")
