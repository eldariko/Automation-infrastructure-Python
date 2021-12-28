import allure
from extensions.apiactions import APIActions


@allure.step("get_request")
def get_request(url):
    response = APIActions.get(url)
    return response


@allure.step("post_request")
def post_request(url, payload):
    response = APIActions.post(url, payload)
    return response


@allure.step("delete_request")
def delete_request(url, id):
    response = APIActions.delete(url, id)
    return response
