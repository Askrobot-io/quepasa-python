# coding: utf-8

"""
    QuePasa RAG SaaS API

    API for RAG retrieval, managing documents, files, and related operations including Telegram integration.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from quepasa.models.setup_telegram_request_commands_ask import SetupTelegramRequestCommandsAsk

class TestSetupTelegramRequestCommandsAsk(unittest.TestCase):
    """SetupTelegramRequestCommandsAsk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SetupTelegramRequestCommandsAsk:
        """Test SetupTelegramRequestCommandsAsk
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SetupTelegramRequestCommandsAsk`
        """
        model = SetupTelegramRequestCommandsAsk()
        if include_optional:
            return SetupTelegramRequestCommandsAsk(
                name = '',
                message = ''
            )
        else:
            return SetupTelegramRequestCommandsAsk(
        )
        """

    def testSetupTelegramRequestCommandsAsk(self):
        """Test SetupTelegramRequestCommandsAsk"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
