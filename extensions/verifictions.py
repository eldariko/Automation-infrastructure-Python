import allure
from softest import TestCase


class Verification:

    @staticmethod
    @allure.step("this method from Verification class verify if actual element is equal to the expected")
    def verify_equal(actual, expected):
        assert actual == expected, "Test Failed"

    @staticmethod
    @allure.step("this method from Verification class verify if actual element is displayed on the screen")
    def verify_true(actual):
        assert actual.is_displayed(), "Test Failed"

    @staticmethod
    @allure.step("this method from Verification class verify with softest if actual element is displayed on the screen")
    def soft_assert_true(actual):
        TestCase.assertTrue(actual, "Test Failed")

    @staticmethod
    @allure.step("this method from Verification class verify with softest if actual element is equal to the expected")
    def soft_assert_equal(actual, expected):
        TestCase.assertEqual(actual, expected, "Test Failed")


