import pytest
from applitools.common import DiffsFoundError

from extensions import ui_actions
from utils import database_reader
from utils.csv_reader import read_test_data_from_csv
from utils.managers.manage_pages import ManagePages
from workflows import web_flows


def login(user_name, password, expected):
    web_flows.login_flow(user_name, password)
    assert expected == web_flows.get_user_name_txt()


@pytest.mark.usefixtures("my_web_starter", "my_web_before_method", "db_set_up")
class TestWeb:

    @pytest.mark.parametrize("user_name, password,expected",
                             read_test_data_from_csv(r'C:\Users\bizyb\PycharmProjects\project\DDTFiles\web.csv'))
    @pytest.mark.order("first")
    def test_login(self, user_name, password, expected):
        login(user_name, password, expected)

    @pytest.mark.parametrize("bank_name,routing_number,account_number,expected",
                             read_test_data_from_csv(
                                 r'C:\Users\bizyb\PycharmProjects\project\DDTFiles\bank_accounts.csv'))
    def test_create_bank_account(self, bank_name, routing_number, account_number, expected):
        web_flows.go_to_bank_account_creation()
        web_flows.create_bank_account(bank_name, routing_number, account_number)
        assert ui_actions.get_element_text(ManagePages.mp.txt_bank_name(bank_name)) == bank_name

    @pytest.mark.parametrize("contact_name,amount,note,action",
                             read_test_data_from_csv(
                                 r'C:\Users\bizyb\PycharmProjects\project\DDTFiles\transactions.csv'))
    def test_create_payment(self, contact_name, amount, note, action):
        balance_before = web_flows.get_account_balance()
        web_flows.create_new_transaction(contact_name, amount, note, action)
        balance_after = web_flows.get_account_balance()
        assert balance_before == balance_after + float(amount)

    @pytest.mark.parametrize("user_name, password, expected",
                             database_reader.read_test_data_from_db())
    def test_login_with_db_params(self, user_name, password, expected):
        login(user_name, password, expected)

    @pytest.mark.usefixtures("eyes", "runner")
    @pytest.mark.order(after="test_login")
    def test_dismiss_notification(self, eyes, runner):
        web_flows.get_notifications_tab()
        eyes.check_window('Screen Shot before dismiss')
        web_flows.dismiss_notification("notification_name")
        eyes.check_window('Screen Shot after notification dismissed')
        eyes.close(False)
        try:
            runner.get_all_test_results(should_raise_exception=True)
        except DiffsFoundError:
            print("Test passed. changes have been founds!")

    @pytest.mark.parametrize("first_name,last_name,user_name,password,expected",
                             read_test_data_from_csv(r'C:\Users\bizyb\PycharmProjects\project\DDTFiles\users.csv'))
    def test_register(self, first_name, last_name, user_name, password, expected):
        web_flows.register_flow(first_name, last_name, user_name, password)
        print(expected)
        assert web_flows.is_text_present(expected) is True
