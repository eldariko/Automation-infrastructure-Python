import allure
import pytest
import softest

from extensions import ui_actions
from extensions.verifictions import Verification
from utils.common_ops import get_data
from utils.managers.manage_pages import ManagePages
from workflows import mobile_flows


@pytest.mark.usefixtures("my_mobile_starter")
class Test_Mobile(softest.TestCase):

    @allure.title("Time Value Of Money Calculator")
    @allure.description("filling text editors with keys and checking history data is presented")
    def test_01tvm_calculator(self):
        mobile_flows.enter_tvm_calc()
        mobile_flows.on_tvm_calc_enter_keys_and_save(get_data("test_01present_value"),
                                                     get_data("test_01payment"),
                                                     get_data("test_01future_value"),
                                                     get_data("test_01annual_rate"),
                                                     get_data("test_01periods"))
        mobile_flows.on_tvm_calc_check_history()
        mobile_flows.on_tvm_calc_go_back()
        self.assert_all()

    @allure.title("Currency Converter")
    @allure.description("filling text editors with keys and checking red massages data and graph is presented")
    def test_02currency_converter(self):
        mobile_flows.enter_currency_converter()
        mobile_flows.on_currency_converter_enter_keys_and_calculate(get_data("test_02rate"),
                                                                    get_data("test_02amount"))
        Verification.soft_assert_true(
            ui_actions.get_element_text(ManagePages.currency_converter_page.get_big_red_txt()))
        Verification.soft_assert_true(
            ui_actions.get_element_text(ManagePages.currency_converter_page.get_small_red_txt()))
        Verification.soft_assert_true(ui_actions.get_element_text(ManagePages.currency_converter_page.get_graph_img()))
        mobile_flows.on_currency_converter_go_back()
        self.assert_all()

    @allure.title("Loan Calculator")
    @allure.description("filling text editors with keys and checking red massages data is presented")
    def test_03loan_calculator(self):
        mobile_flows.enter_loan_calc()
        mobile_flows.on_loan_calc_enter_keys_and_calculate(get_data("test_03amount"),
                                                           get_data("test_03interest_rate"),
                                                           get_data("test_03loan_term_years"),
                                                           get_data("test_03loan_term_months"),
                                                           get_data("test_03extra_payment"))
        mobile_flows.on_loan_calc_check_red_massage()
        mobile_flows.on_loan_calc_go_back()
        self.assert_all()

    @allure.title("Compound Interest Calculator")
    @allure.description("filling text editors with keys and checking red massages data is presented")
    def test_04compound_interest_calculator(self):
        mobile_flows.enter_compound_interest_calc()
        mobile_flows.on_compound_interest_enter_keys_and_calculate(get_data("test_04principal_amount"),
                                                                   get_data("test_04monthly_deposit"),
                                                                   get_data("test_04period"),
                                                                   get_data("test_04annual_interest_rate"))
        mobile_flows.on_compound_interest_check_red_massages()
        mobile_flows.on_compound_interest_go_back()
        self.assert_all()

    @allure.title("Credit Card Payoff Calculator")
    @allure.description("filling text editors with keys and checking red massages data is presented")
    def test_05credit_card_payoff(self):
        mobile_flows.enter_payoff_calc()
        mobile_flows.on_payoff_calc_enter_keys_and_calculate(get_data("test_05cc_balance"),
                                                             get_data("test_05cc_interest"),
                                                             get_data("test_05payment_per_month"))
        mobile_flows.on_payoff_calc_check_red_massage()
        mobile_flows.on_payoff_calc_go_back()
        self.assert_all()
