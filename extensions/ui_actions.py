from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec

import testcases.conftest


def click(locator: tuple):
    testcases.conftest.wait.until(ec.element_to_be_clickable(locator)).click()


def set_text(locator: tuple, text):
    elem: WebElement = testcases.conftest.wait.until(ec.visibility_of_element_located(locator))
    elem.clear()
    elem.send_keys(text)


def is_text_present(locator: tuple, text):
    return testcases.conftest.wait.until(ec.text_to_be_present_in_element(locator, text))


def get_element_text(locator: tuple):
    return testcases.conftest.wait.until(ec.visibility_of_element_located(locator)).text


def get_element_list(locator: tuple):
    return testcases.conftest.wait.until(ec.visibility_of_all_elements_located(locator))
