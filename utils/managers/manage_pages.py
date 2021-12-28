from page_objects.desktop.calculator_page import Calculator_Page
from page_objects.electron.apidemos_page import Apidemos_Page
from page_objects.mobile import TvmCalcPage, CurrencyConverterPage, LoanCalcPage, CompoundInterestCalcPage
from page_objects.mobile.TvmCalcPage import TvmCalcPage
from page_objects.mobile.CurrencyConverterPage import CurrencyConverterPage
from page_objects.mobile.LoanCalcPage import LoanCalcPage
from page_objects.mobile.CompoundInterestCalcPage import CompoundInterestCalcPage
from page_objects.mobile.PayOffCalcPage import PayOffCalcPage
from page_objects.mobile.MobileMainPage import MobileMainPage
from page_objects.web.create_bank_account_page import CreateBankAccountPage
from page_objects.web.login_page import LoginPage
from page_objects.web.notifications_page import NotificationsPage
from page_objects.web.sign_up_page import SignUpPage
from page_objects.web.web_main_page import WebMainPage


class ManagePages:
    tvm_calc_page: TvmCalcPage
    currency_converter_page: CurrencyConverterPage
    loan_calc_page: LoanCalcPage
    compound_interest_calc_page: CompoundInterestCalcPage
    pay_off_calc_page: PayOffCalcPage
    main_page: MobileMainPage
    #
    lp: LoginPage
    su: SignUpPage
    mp: WebMainPage
    cba: CreateBankAccountPage
    np: NotificationsPage
    #
    cl: Calculator_Page
    demo: Apidemos_Page

    @classmethod
    def init_desktop_page(cls, driver):
        cls.cl = Calculator_Page(driver)

    @classmethod
    def init_electron_page(cls, driver):
        cls.demo = Apidemos_Page(driver)

    @classmethod
    def init_mobile_pages(cls, driver):
        cls.tvm_calc_page = TvmCalcPage(driver)
        cls.currency_converter_page = CurrencyConverterPage(driver)
        cls.loan_calc_page = LoanCalcPage(driver)
        cls.compound_interest_calc_page = CompoundInterestCalcPage(driver)
        cls.pay_off_calc_page = PayOffCalcPage(driver)
        cls.main_page = MobileMainPage(driver)

    @classmethod
    def init_web_pages(cls, driver):
        cls.lp = LoginPage(driver)
        cls.su = SignUpPage(driver)
        cls.mp = WebMainPage(driver)
        cls.cba = CreateBankAccountPage(driver)
        cls.np = NotificationsPage(driver)
