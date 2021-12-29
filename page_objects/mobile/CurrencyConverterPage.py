from selenium.webdriver.common.by import By


def get_rate_edit_txt():
    return By.XPATH, "//*[@id='exchRateInput']"


def get_amount_edit_txt():
    return By.XPATH, "//*[@id='amountInput']"


def get_big_red_txt():
    return By.XPATH, "//*[@text='3 USD = 150 EUR']"


def get_small_red_txt():
    return By.XPATH, "//*[@text='3 EUR = 0.06 USD']"


def get_graph_img():
    return By.XPATH, "//*[@id='exChart']"


def get_back_btn():
    return By.XPATH, "//android.widget.ImageButton"
