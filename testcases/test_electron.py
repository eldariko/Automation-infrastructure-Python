import allure
import pytest

from extensions.actions import UIActions
from page_objects.electron import apidemos_page
from workflows import electron_flows
from extensions.verifictions import Verification


@pytest.mark.usefixtures("my_electron_starter")
class TestElectron:

    @allure.title("testing electron")
    @allure.description("Test Customize Menus btn ")
    def test_01(self):
        electron_flows.click_menuus()
        Verification.verify_equal(UIActions.get_element_text(apidemos_page.cust_me()), 'Customize Menus')
