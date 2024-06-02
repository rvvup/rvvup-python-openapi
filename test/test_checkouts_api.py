# coding: utf-8

"""
    Rvvup API

    Rvvup Public API

    The version of the OpenAPI document: 2024-03-01
    Contact: info@rvvup.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.checkouts_api import CheckoutsApi


class TestCheckoutsApi(unittest.TestCase):
    """CheckoutsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CheckoutsApi()

    def tearDown(self) -> None:
        pass

    def test_create_checkout(self) -> None:
        """Test case for create_checkout

        Create new checkout
        """
        pass

    def test_get_checkout(self) -> None:
        """Test case for get_checkout

        Get a checkout
        """
        pass

    def test_list_checkout_payment_methods(self) -> None:
        """Test case for list_checkout_payment_methods

        Get payment methods for a checkout
        """
        pass

    def test_list_checkouts(self) -> None:
        """Test case for list_checkouts

        List checkouts
        """
        pass


if __name__ == '__main__':
    unittest.main()