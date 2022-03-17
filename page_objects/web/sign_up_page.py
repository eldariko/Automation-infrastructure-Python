from selenium.webdriver.common.by import By


def input_first_name():
    return By.ID, "firstName"


def input_last_name():
    return By.ID, "lastName"


def input_user_name():
    return By.ID, "username"


def input_password():
    return By.ID, "password"


def input_confirm_password():
    return By.ID, "confirmPassword"


def button_sign_up():
    return By.XPATH, "//span[text()='Sign Up']"
