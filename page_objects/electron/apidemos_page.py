from selenium.webdriver.common.by import By


def get_btn_menuus():
    return By.ID, "button-menus"


def get_btn_windows():
    return By.ID, "button-windows"


def get_btn_crash():
    return By.ID, "button-crash-hang"


# def get_nav_itemes(self):
#
#     return len(self.driver.find_elements_by_class_name("nav-item u-category"))

def cust_me():
    return By.XPATH, "// *[ @ id = 'menus-section'] / header / div / h1"
