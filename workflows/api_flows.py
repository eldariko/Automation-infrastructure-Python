import allure
from extensions.api_actions import APIActions


@allure.step("get_request")
def get_request(url):
    response = APIActions.get(url)
    return response


@allure.step("post_request")
def post_request(url, payload):
    response = APIActions.post(url, payload)
    return response


@allure.step("delete_request")
def delete_request(url, user_id):
    response = APIActions.delete(url, user_id)
    return response
