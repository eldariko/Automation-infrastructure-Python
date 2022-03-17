from selenium.webdriver.common.by import By


def txt_user_name():
    return By.XPATH, "//h6[@data-test='sidenav-username']"


#
#
# def input_user_name(self):
#     return self.driver.find_element_by_id("username")
#
#
# def input_password(self):
#     return self.driver.find_element_by_id("password")
#
#
# def input_confirm_password(self):
#     return self.driver.find_element_by_id("confirmPassword")
#
#
# def button_sign_up(self):
#     return self.driver.find_element_by_xpath("//span[text()='Sign Up']")


def txt_get_started():
    return By.XPATH, "//h2[text()='Get Started with Real World App']"


def tab_bank_acoount():
    return By.XPATH, "//span[text()='Bank Accounts']"


def tab_notifications():
    return By.XPATH, "//span[text()='Notifications']"


def button_create():
    return By.XPATH, "//span[text()='Create']"


def txt_bank_name(bank_name):
    return By.XPATH, f"//p[@class='MuiTypography-root MuiTypography-body1 MuiTypography-colorPrimary " \
                     f"MuiTypography-gutterBottom'][text()='{bank_name}'] "


def button_new_transaction():
    return By.XPATH, "//span[text()=' New']"


def button_contact_name(contact_name):
    return By.XPATH, f"//span[text()='{contact_name}']"


def input_amount():
    return By.ID, "amount"


def input_note():
    return By.ID, "transaction-create-description-input"


def button_action(action):
    return By.XPATH, f"//span[text()='{action}']"


def txt_account_balance():
    return By.XPATH, "//h6[@data-test='sidenav-user-balance']"
