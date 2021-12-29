import allure

from extensions.actions import UIActions
from page_objects.desktop import calculator_page


@allure.step("Desktop calculator addition ")
def addition():
    UIActions.click(calculator_page.get_clear())
    UIActions.click(calculator_page.get_two())
    UIActions.click(calculator_page.get_multi())
    UIActions.click(calculator_page.get_seven())
    UIActions.click(calculator_page.get_equels())
