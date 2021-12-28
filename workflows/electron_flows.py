import allure

from extensions import electron_actions
from utils.managers.manage_pages import ManagePages


@allure.step("click on btn menuus")
def click_menuus():
    electron_actions.click(ManagePages.demo.get_btn_menuus())

    # electron_actions.click(ManagePages.demo.get_btn_crash())

    # electron_actions.click(ManagePages.demo.get_btn_windows())
