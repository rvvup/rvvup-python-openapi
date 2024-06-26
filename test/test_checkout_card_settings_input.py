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

from openapi_client.models.checkout_card_settings_input import CheckoutCardSettingsInput

class TestCheckoutCardSettingsInput(unittest.TestCase):
    """CheckoutCardSettingsInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CheckoutCardSettingsInput:
        """Test CheckoutCardSettingsInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CheckoutCardSettingsInput`
        """
        model = CheckoutCardSettingsInput()
        if include_optional:
            return CheckoutCardSettingsInput(
                capture_type = 'AUTOMATIC_CHECKOUT',
                customer_fields = openapi_client.models.checkout_customer_fields_input.CheckoutCustomerFieldsInput(
                    optional = [
                        'GIVEN_NAME'
                        ], 
                    required = [
                        'GIVEN_NAME'
                        ], )
            )
        else:
            return CheckoutCardSettingsInput(
        )
        """

    def testCheckoutCardSettingsInput(self):
        """Test CheckoutCardSettingsInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
