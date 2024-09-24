# coding: utf-8

"""
    QuePasa RAG SaaS API

    API for RAG retrieval, managing documents, files, and related operations including Telegram integration.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from quepasa.models.document_detail_data import DocumentDetailData

class TestDocumentDetailData(unittest.TestCase):
    """DocumentDetailData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DocumentDetailData:
        """Test DocumentDetailData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DocumentDetailData`
        """
        model = DocumentDetailData()
        if include_optional:
            return DocumentDetailData(
                id = '',
                url = '',
                domain = '',
                title = '',
                keywords = '',
                pages = [
                    quepasa.models.document_detail_data_pages_inner.DocumentDetail_data_pages_inner(
                        text = '', 
                        language = '', 
                        keywords = '', )
                    ],
                languages = [
                    ''
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return DocumentDetailData(
                id = '',
                url = '',
                domain = '',
                title = '',
                keywords = '',
                pages = [
                    quepasa.models.document_detail_data_pages_inner.DocumentDetail_data_pages_inner(
                        text = '', 
                        language = '', 
                        keywords = '', )
                    ],
                languages = [
                    ''
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testDocumentDetailData(self):
        """Test DocumentDetailData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()