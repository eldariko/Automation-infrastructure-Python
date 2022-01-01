import allure
import requests


class APIActions:

    @staticmethod
    @allure.step("get posts")
    def get(url):
        response = requests.get(url)
        return response

    @staticmethod
    @allure.step("post one post")
    def post(url, payload):
        response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
        return response

    @staticmethod
    @allure.step("delete post by ID")
    def delete(url, user_id):
        s = f"{url}/{user_id}"
        response = requests.delete(s)
        return response
