import allure

from extensions.actions import MobileAction
from extensions.verifictions import Verification
from page_objects.mobile import TvmCalcPage, MobileMainPage, PayOffCalcPage, CompoundInterestCalcPage, LoanCalcPage, \
    CurrencyConverterPage


@allure.step("this func enters into the tvm calc page")
def enter_tvm_calc():
    MobileAction.mobile_click(MobileMainPage.get_tvm_calc())


@allure.step("this func puts in the tvm calculator some keys into the txt fields and than saving info")
def on_tvm_calc_enter_keys_and_save(present_value, payment, future_value, annual_rate, periods):
    MobileAction.mobile_send_keys(TvmCalcPage.get_present_value_edit_txt(), present_value)
    MobileAction.mobile_send_keys(TvmCalcPage.get_payment_edit_txt(), payment)
    MobileAction.mobile_send_keys(TvmCalcPage.get_future_value_edit_txt(), future_value)
    MobileAction.mobile_send_keys(TvmCalcPage.get_annual_rate_edit_txt(), annual_rate)
    MobileAction.mobile_send_keys(TvmCalcPage.get_periods_edit_txt(), periods)
    MobileAction.mobile_click(TvmCalcPage.get_beginning_radio_btn())
    MobileAction.mobile_click(TvmCalcPage.get_four_radio_btn())
    MobileAction.mobile_click(TvmCalcPage.get_save_btn())


@allure.step("this func enters into the history and checks if there is history inside")
def on_tvm_calc_check_history():
    MobileAction.mobile_click(TvmCalcPage.get_history_btn())
    Verification.soft_assert_true(TvmCalcPage.get_history_txt_view())


@allure.step("this func takes us from tvm calculator to the main page")
def on_tvm_calc_go_back():
    MobileAction.mobile_click(TvmCalcPage.get_back_btn())
    MobileAction.mobile_click(TvmCalcPage.get_back_btn())


# ****************************************CURRENCY-CONVERTER*******************************************
@allure.step("this func enters the currency converter calculator")
def enter_currency_converter():
    MobileAction.click(MobileMainPage.get_currency_converter())


@allure.step("this func puts in the currency converter calculator some keys into the text fields")
def on_currency_converter_enter_keys_and_calculate(rate, amount):
    MobileAction.set_text(CurrencyConverterPage.get_rate_edit_txt(), rate)
    MobileAction.set_text(CurrencyConverterPage.get_amount_edit_txt(), amount)


@allure.step("this func takes us from currency converter calculator to the main page")
def on_currency_converter_go_back():
    MobileAction.click(CurrencyConverterPage.get_back_btn())


# ****************************************LOAN-CALC*******************************************
@allure.step("this func enters the loan calculator")
def enter_loan_calc():
    MobileAction.mobile_click(MobileMainPage.get_loan_calc())


@allure.step("this func puts in the loan calculator some keys and clicks on the calculate button")
def on_loan_calc_enter_keys_and_calculate(amount, interest_rate, loan_term_years, loan_term_months, extra_payment):
    MobileAction.mobile_send_keys(LoanCalcPage.get_amount_edit_txt(), amount)
    MobileAction.mobile_send_keys(LoanCalcPage.get_interest_rate_edit_txt(), interest_rate)
    MobileAction.mobile_send_keys(LoanCalcPage.get_loan_term_years_edit_txt(), loan_term_years)
    MobileAction.mobile_send_keys(LoanCalcPage.get_loan_term_months_edit_txt(), loan_term_months)
    MobileAction.mobile_send_keys(LoanCalcPage.get_extra_payment_per_month_edit_txt(), extra_payment)
    MobileAction.mobile_click(LoanCalcPage.get_calc_btn())


@allure.step("this func checks in the loan calculator if there is red massages  with a results")
def on_loan_calc_check_red_massage():
    Verification.soft_assert_true(LoanCalcPage.get_monthly_payment_txt_view())
    Verification.soft_assert_true(LoanCalcPage.get_total_payment_txt_view())
    Verification.soft_assert_true(LoanCalcPage.get_total_interest_txt_view())
    Verification.soft_assert_true(LoanCalcPage.get_annual_payment_txt_view())
    Verification.soft_assert_true(LoanCalcPage.get_mortgage_constant_txt_view())
    Verification.soft_assert_true(LoanCalcPage.get_interest_saving_txt_view())
    Verification.soft_assert_true(LoanCalcPage.get_payoff_earlier_txt_view())


@allure.step("this func takes us from loan calculator to the main page")
def on_loan_calc_go_back():
    MobileAction.mobile_click(LoanCalcPage.get_back_btn())


# ****************************************COMPOUND-INTEREST-CALC*******************************************
@allure.step("this func enters the compound interest calculator")
def enter_compound_interest_calc():
    MobileAction.mobile_click(MobileMainPage.get_compound_interest_calc())


@allure.step("this func puts in the compound interest calculator some keys and clicks on the calculate button")
def on_compound_interest_enter_keys_and_calculate(principal_amount, monthly_deposit, period, annual_interest_rate):
    MobileAction.mobile_send_keys(CompoundInterestCalcPage.get_principal_amount_edit_txt(),
                                  principal_amount)
    MobileAction.mobile_send_keys(CompoundInterestCalcPage.get_monthly_deposit_edit_txt(),
                                  monthly_deposit)
    MobileAction.mobile_send_keys(CompoundInterestCalcPage.get_period_edit_txt(), period)
    MobileAction.mobile_send_keys(CompoundInterestCalcPage.get_annual_interest_rate_edit_txt(),
                                  annual_interest_rate)
    MobileAction.mobile_click(CompoundInterestCalcPage.get_calc_btn())


@allure.step("this func checks in the compound interest calculator if there is red massages  with a results")
def on_compound_interest_check_red_massages():
    Verification.soft_assert_true(CompoundInterestCalcPage.get_total_principal_txt_view())
    Verification.soft_assert_true(CompoundInterestCalcPage.get_interest_amount_txt_view())
    Verification.soft_assert_true(CompoundInterestCalcPage.get_maturity_value_txt_view())
    Verification.soft_assert_true(CompoundInterestCalcPage.get_apy_txt_view())


@allure.step("this func takes us from compound interest calculator to the main page")
def on_compound_interest_go_back():
    MobileAction.mobile_click(CompoundInterestCalcPage.get_back_btn())


# ****************************************PAYOFF-CALC*******************************************
@allure.step("this func enters the payoff calculator")
def enter_payoff_calc():
    MobileAction.mobile_click(MobileMainPage.get_cc_payoff_calc())


@allure.step("this func puts in the payoff calculator  some keys and clicks on the calculate button")
def on_payoff_calc_enter_keys_and_calculate(cc_balance, cc_interest, payment_per_month):
    MobileAction.mobile_send_keys(PayOffCalcPage.get_cc_balance_edit_txt(), cc_balance)
    MobileAction.mobile_send_keys(PayOffCalcPage.get_cc_interest_edit_txt(), cc_interest)
    MobileAction.mobile_send_keys(PayOffCalcPage.get_payment_per_month_edit_txt(), payment_per_month)
    MobileAction.mobile_click(PayOffCalcPage.get_calc_btn())


@allure.step("this func checks in the payoff calculator if there is red massage with a result")
def on_payoff_calc_check_red_massage():
    Verification.soft_assert_true(PayOffCalcPage.get_result())


@allure.step("this func takes us from payoff calculator to the main page")
def on_payoff_calc_go_back():
    MobileAction.mobile_click(PayOffCalcPage.get_back_btn())
