import random

from extensions import ui_actions
from utils.managers.manage_pages import ManagePages


def login_flow(user_name, password):
    ui_actions.set_text(ManagePages.lp.locator_input_user_name, user_name)
    ui_actions.set_text(ManagePages.lp.locator_input_password, password)
    ui_actions.click(ManagePages.lp.locator_button_sign_in)


def get_user_name_txt():
    return ManagePages.mp.txt_user_name().text


def is_text_present(text):
    return ui_actions.is_text_present(ManagePages.mp.txt_get_started(), text)


def go_to_bank_account_creation():
    ui_actions.click(ManagePages.mp.tab_bank_acoount())
    ui_actions.click(ManagePages.mp.button_create())


def register_flow(first_name, last_name, user_name, password):
    e = ManagePages.lp.locator_link_sign_up
    ui_actions.click(e)
    ui_actions.click(e)
    ui_actions.set_text(ManagePages.su.locator_input_first_name, first_name)
    ui_actions.set_text(ManagePages.su.locator_input_last_name, last_name)
    ui_actions.set_text(ManagePages.su.locator_input_user_name, user_name)
    ui_actions.set_text(ManagePages.su.locator_input_password, password)
    ui_actions.set_text(ManagePages.su.locator_input_confirm_password, password)
    ui_actions.click(ManagePages.su.locator_button_sign_up)
    login_flow(user_name, password)


def create_bank_account(bank_name, routing_number, account_number):
    ui_actions.set_text(ManagePages.cba.locator_bank_name(), bank_name)
    ui_actions.set_text(ManagePages.cba.locator_routing_number(), routing_number)
    ui_actions.set_text(ManagePages.cba.locator_account_number(), account_number)
    ui_actions.click(ManagePages.cba.locator_button_save())


def create_new_transaction(contact_name, amount, note, action):
    ui_actions.click(ManagePages.mp.button_new_transaction())
    ui_actions.click(ManagePages.mp.button_contact_name(contact_name))
    ui_actions.set_text(ManagePages.mp.input_amount(), amount)
    ui_actions.set_text(ManagePages.mp.input_note(), note)
    ui_actions.click(ManagePages.mp.button_action(action))


def get_account_balance():
    import re
    balance: str = ui_actions.get_element_text(ManagePages.mp.txt_account_balance())
    balance = re.sub(f"[,$]", '', balance)
    return float(balance)


def dismiss_notification(notification_name):
    web_elems = ui_actions.get_element_list(ManagePages.np.button_dismis())
    i = random.randint(0, len(web_elems) - 1)
    web_elems[i].click()


def get_notifications_tab():
    ui_actions.click(ManagePages.mp.tab_notifications())
