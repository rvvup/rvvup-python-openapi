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

from openapi_client.models.webhook import Webhook

class TestWebhook(unittest.TestCase):
    """Webhook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Webhook:
        """Test Webhook
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Webhook`
        """
        model = Webhook()
        if include_optional:
            return Webhook(
                headers = {
                    'key' : ''
                    },
                id = '',
                merchant_id = '',
                status = 'ENABLED',
                subscribed_events = [
                    '["PAYMENT_SUCCEEDED"]'
                    ],
                url = ''
            )
        else:
            return Webhook(
                headers = {
                    'key' : ''
                    },
                id = '',
                merchant_id = '',
                status = 'ENABLED',
                subscribed_events = [
                    '["PAYMENT_SUCCEEDED"]'
                    ],
                url = '',
        )
        """

    def testWebhook(self):
        """Test Webhook"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
