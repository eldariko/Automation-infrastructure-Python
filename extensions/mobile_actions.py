import allure

import testcases.conftest


class MobileAction:
    @staticmethod
    @allure.step("this method from MobileAction class sends keys to an element")
    def mobile_send_keys(elem, keys):
        testcases.conftest.wait()
        elem.send_keys(keys)

    @staticmethod
    @allure.step("this method from MobileAction class clicks on element")
    def mobile_click(elem):
        elem.click()
