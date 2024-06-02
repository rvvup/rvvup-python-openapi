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

from openapi_client.models.webhook_create_input import WebhookCreateInput

class TestWebhookCreateInput(unittest.TestCase):
    """WebhookCreateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookCreateInput:
        """Test WebhookCreateInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookCreateInput`
        """
        model = WebhookCreateInput()
        if include_optional:
            return WebhookCreateInput(
                headers = {
                    'key' : ''
                    },
                subscribed_events = ["PAYMENT_SUCCEEDED","REFUND_SUCCEEDED"],
                url = 'https://example.com/webhook'
            )
        else:
            return WebhookCreateInput(
                headers = {
                    'key' : ''
                    },
                subscribed_events = ["PAYMENT_SUCCEEDED","REFUND_SUCCEEDED"],
                url = 'https://example.com/webhook',
        )
        """

    def testWebhookCreateInput(self):
        """Test WebhookCreateInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()