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

from openapi_client.models.item import Item

class TestItem(unittest.TestCase):
    """Item unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Item:
        """Test Item
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Item`
        """
        model = Item()
        if include_optional:
            return Item(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                name = '',
                price = openapi_client.models.money.Money(
                    amount = '', 
                    currency = '', ),
                price_with_tax = openapi_client.models.money.Money(
                    amount = '', 
                    currency = '', ),
                quantity = '',
                restriction = 'ALLOWED',
                sku = '',
                tax = openapi_client.models.money.Money(
                    amount = '', 
                    currency = '', ),
                total = openapi_client.models.money.Money(
                    amount = '', 
                    currency = '', )
            )
        else:
            return Item(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                name = '',
                price = openapi_client.models.money.Money(
                    amount = '', 
                    currency = '', ),
                quantity = '',
                restriction = 'ALLOWED',
                sku = '',
                total = openapi_client.models.money.Money(
                    amount = '', 
                    currency = '', ),
        )
        """

    def testItem(self):
        """Test Item"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()