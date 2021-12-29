import random

from extensions.actions import UIActions
from page_objects.web import login_page, web_main_page, sign_up_page, notifications_page, create_bank_account_page


def login_flow(user_name, password):
    UIActions.set_text(login_page.input_user_name(), user_name)
    UIActions.set_text(login_page.input_password(), password)
    UIActions.click(login_page.button_sign_in())


def is_text_present(text):
    return UIActions.is_text_present(web_main_page.txt_get_started(), text)


def go_to_bank_account_creation():
    UIActions.click(web_main_page.tab_bank_acoount())
    UIActions.click(web_main_page.button_create())


def register_flow(first_name, last_name, user_name, password):
    e = login_page.link_sign_up()
    UIActions.click(e)
    UIActions.click(e)
    UIActions.set_text(sign_up_page.input_first_name(), first_name)
    UIActions.set_text(sign_up_page.input_last_name(), last_name)
    UIActions.set_text(sign_up_page.input_user_name(), user_name)
    UIActions.set_text(sign_up_page.input_password(), password)
    UIActions.set_text(sign_up_page.input_confirm_password(), password)
    UIActions.click(sign_up_page.button_sign_up())
    login_flow(user_name, password)


def create_bank_account(bank_name, routing_number, account_number):
    UIActions.set_text(create_bank_account_page.locator_bank_name(), bank_name)
    UIActions.set_text(create_bank_account_page.locator_routing_number(), routing_number)
    UIActions.set_text(create_bank_account_page.locator_account_number(), account_number)
    UIActions.click(create_bank_account_page.locator_button_save())


def create_new_transaction(contact_name, amount, note, action):
    UIActions.click(web_main_page.button_new_transaction())
    UIActions.click(web_main_page.button_contact_name(contact_name))
    UIActions.set_text(web_main_page.input_amount(), amount)
    UIActions.set_text(web_main_page.input_note(), note)
    UIActions.click(web_main_page.button_action(action))


def get_account_balance():
    import re
    balance: str = UIActions.get_element_text(web_main_page.txt_account_balance())
    balance = re.sub(f"[,$]", '', balance)
    return float(balance)


def dismiss_notification():
    web_elems = UIActions.get_element_list(notifications_page.button_dismis())
    i = random.randint(0, len(web_elems) - 1)
    web_elems[i].click()


def get_notifications_tab():
    UIActions.click(web_main_page.tab_notifications())
