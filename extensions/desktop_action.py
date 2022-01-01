from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec

import testcases.conftest


def click(ele: WebElement):
    ele.click()
    # test_cases.conftest.wait.until(ec.element_to_be_clickable(locator)).click()
