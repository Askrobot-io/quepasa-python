# coding: utf-8

"""
    QuePasa RAG SaaS API

    API for RAG retrieval, managing documents, files, and related operations including Telegram integration.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from quepasa.models.created_batch_status import CreatedBatchStatus

class TestCreatedBatchStatus(unittest.TestCase):
    """CreatedBatchStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreatedBatchStatus:
        """Test CreatedBatchStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreatedBatchStatus`
        """
        model = CreatedBatchStatus()
        if include_optional:
            return CreatedBatchStatus(
                status = '',
                data = quepasa.models.created_batch_status_data.CreatedBatchStatus_data(
                    batch_id = '', 
                    processed_ids = [
                        ''
                        ], )
            )
        else:
            return CreatedBatchStatus(
                status = '',
                data = quepasa.models.created_batch_status_data.CreatedBatchStatus_data(
                    batch_id = '', 
                    processed_ids = [
                        ''
                        ], ),
        )
        """

    def testCreatedBatchStatus(self):
        """Test CreatedBatchStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()