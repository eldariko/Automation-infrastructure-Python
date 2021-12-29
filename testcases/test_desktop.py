import allure
import pytest

from extensions.actions import UIActions
from extensions.verifictions import Verification
from page_objects.desktop import calculator_page
from utils.common_ops import get_data
from workflows import desktop_flows

result = get_data("excepted_result_desktop")


@pytest.mark.usefixtures("my_desktop_starter")
class TestDesktop:

    @allure.title("testing calculator")
    @allure.description("Test adding functionality ")
    def test_01(self):
        desktop_flows.addition()
        Verification.verify_equal(UIActions.get_element_text(calculator_page.get_result()), result)
