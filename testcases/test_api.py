import json

import allure
from extensions.verifictions import Verification
from workflows import api_flows

from utils.common_ops import get_data

url = get_data("apiUrl")
id = get_data("id_post")
# payload = {"userId": 12, "id": "103", "title": "test", "body": "123"}


payload = json.loads(get_data("payload"))


class Test_Api_Server:
    @allure.title("testing API -GET")
    @allure.description("get all the posts from json:server")
    def test_01_get_post_list(self):
        response = api_flows.get_request(url)
        Verification.verify_equal(response.status_code, 200)

    @allure.title("testing API -POST")
    @allure.description("post to json:server ")
    def test_02_create_post(self):
        response = api_flows.post_request(url, payload)
        Verification.verify_equal(response.status_code, 201)

    @allure.title("testing API -DELETE")
    @allure.description("delete post from  json:server by ID ")
    def test_03_delete_post(self):
        response = api_flows.delete_request(url, id)
        Verification.verify_equal(response.status_code, 200)
