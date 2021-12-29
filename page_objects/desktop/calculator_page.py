from selenium.webdriver.common.by import By


def get_two():
    return By.NAME, "Two"

    # return self.driver.find_element_by_name("Two")


def get_seven():
    return By.NAME, "Seven"
    # return self.driver.find_element_by_name("Seven")


def get_clear():
    return By.NAME, "Clear"


def get_equels():
    return By.NAME, "Equals"
    # return self.driver.find_element_by_name("Equals")


def get_multi():
    return By.NAME, "Multiply by"

    # return self.driver.find_element_by_name("Multiply by")


# def get_result(self):
# return By.XPATH, "//*[@AutomationId='CalculatorResults']"

# return self.driver.find_elements_by_xpath("//*[@AutomationId='CalculatorResults']")

def get_result():
    # trim extra text and whitespace off of the display value
    # return self.driver.find_element_by_xpath("//*[@AutomationId='CalculatorResults']").text.replace("Display is",
    #                                                                                                 "").strip()
    return By.XPATH, "//*[@AutomationId='CalculatorResults']"
