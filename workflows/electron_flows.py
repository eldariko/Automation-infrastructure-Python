import allure

from extensions.actions import UIActions
from page_objects.electron import apidemos_page


@allure.step("click on btn menuus")
def click_menuus():
    UIActions.click(apidemos_page.get_btn_menuus())
