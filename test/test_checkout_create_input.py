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

from openapi_client.models.checkout_create_input import CheckoutCreateInput

class TestCheckoutCreateInput(unittest.TestCase):
    """CheckoutCreateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CheckoutCreateInput:
        """Test CheckoutCreateInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CheckoutCreateInput`
        """
        model = CheckoutCreateInput()
        if include_optional:
            return CheckoutCreateInput(
                amount = {"amount":"100.00","currency":"GBP"},
                billing_address = openapi_client.models.address_input.AddressInput(
                    city = 'London', 
                    company = '0', 
                    country_code = 'GB', 
                    line1 = '10 Downing Street', 
                    line2 = 'Westminster', 
                    name = 'John Doe', 
                    phone_number = '0', 
                    postcode = 'SW1A 2AA', 
                    state = 'Greater London', ),
                checkout_template_id = '',
                customer = openapi_client.models.customer_input.CustomerInput(
                    email = '0', 
                    given_name = 'John', 
                    phone_number = '0', 
                    surname = 'Doe', ),
                metadata = {"key1":"value1","key2":"value2"},
                reference = 'Order #12345',
                source = 'API',
                success_url = 'https://example.com/success?checkout_id={{CHECKOUT_ID}}'
            )
        else:
            return CheckoutCreateInput(
        )
        """

    def testCheckoutCreateInput(self):
        """Test CheckoutCreateInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
