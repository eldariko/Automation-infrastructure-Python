import allure
import pytest

from extensions.verifictions import Verification
from utils.common_ops import get_data
from utils.managers.manage_pages import ManagePages
from workflows import desktop_flows

result = get_data("excepted_result_desktop")


@pytest.mark.usefixtures("my_desktop_starter")
class Test_Desktop:

    @allure.title("testing calculator")
    @allure.description("Test adding functionality ")
    def test_01(self):
        desktop_flows.addition()
        Verification.verify_equal(ManagePages.cl.get_result(), result)
