import allure
import pytest
from workflows import electron_flows
from extensions.verifictions import Verification
from utils.managers.manage_pages import ManagePages


@pytest.mark.usefixtures("my_electron_starter")
class Test_Electron:

    @allure.title("testing electron")
    @allure.description("Test Customize Menus btn ")
    def test_01(self):
        electron_flows.click_menuus()
        Verification.verify_equal(ManagePages.demo.cust_me().text, 'Customize Menus')
