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

from openapi_client.models.payment_method_limit import PaymentMethodLimit

class TestPaymentMethodLimit(unittest.TestCase):
    """PaymentMethodLimit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentMethodLimit:
        """Test PaymentMethodLimit
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentMethodLimit`
        """
        model = PaymentMethodLimit()
        if include_optional:
            return PaymentMethodLimit(
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                total = [
                    openapi_client.models.payment_method_total_limit.PaymentMethodTotalLimit(
                        currency = '', 
                        max = '', 
                        min = '', )
                    ]
            )
        else:
            return PaymentMethodLimit(
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                total = [
                    openapi_client.models.payment_method_total_limit.PaymentMethodTotalLimit(
                        currency = '', 
                        max = '', 
                        min = '', )
                    ],
        )
        """

    def testPaymentMethodLimit(self):
        """Test PaymentMethodLimit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()