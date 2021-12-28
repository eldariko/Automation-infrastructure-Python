from selenium.webdriver.common.by import By


class TvmCalcPage:
    def __init__(self, driver):
        self.driver = driver

    def get_present_value_edit_txt(self):
        return self.driver.find_element(By.XPATH, "//*[@id='pvInput']")

    def get_payment_edit_txt(self):
        return self.driver.find_element(By.XPATH, "//*[@id='pmtInput']")

    def get_future_value_edit_txt(self):
        return self.driver.find_element(By.XPATH, "//*[@id='fvInput']")

    def get_annual_rate_edit_txt(self):
        return self.driver.find_element(By.XPATH, "//*[@id='rateInput']")

    def get_periods_edit_txt(self):
        return self.driver.find_element(By.XPATH, "//*[@id='periodInput']")

    def get_beginning_radio_btn(self):
        return self.driver.find_element(By.XPATH, "//*[@text='Beginning']")

    def get_four_radio_btn(self):
        return self.driver.find_element(By.XPATH, "//*[@text='four']")

    def get_save_btn(self):
        return self.driver.find_element(By.XPATH, "//*[@text='SAVE']")

    def get_history_btn(self):
        return self.driver.find_element(By.XPATH, "//*[@text='HISTORY']")

    def get_history_txt_view(self):
        return self.driver.find_element(By.XPATH, "(//*[@id='listview']/*/*[@id='text1'])[1]")

    def get_back_btn(self):
        return self.driver.find_element(By.XPATH, "//*[@contentDescription='Navigate up']")
