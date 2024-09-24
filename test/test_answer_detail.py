# coding: utf-8

"""
    QuePasa RAG SaaS API

    API for RAG retrieval, managing documents, files, and related operations including Telegram integration.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from quepasa.models.answer_detail import AnswerDetail

class TestAnswerDetail(unittest.TestCase):
    """AnswerDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AnswerDetail:
        """Test AnswerDetail
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AnswerDetail`
        """
        model = AnswerDetail()
        if include_optional:
            return AnswerDetail(
                status = '',
                data = quepasa.models.answer_detail_data.AnswerDetail_data(
                    answer = 'LLM stands for Large Language Model. It is a computational model capable of language generation and other natural language processing tasks.', 
                    links = {
                        'key' : quepasa.models.answer_detail_data_links_value.AnswerDetail_data_links_value(
                            id = '', 
                            url = '', 
                            title = '', )
                        }, 
                    markdown = '', 
                    labeled_links = {
                        'key' : quepasa.models.answer_detail_data_labeled_links_value.AnswerDetail_data_labeled_links_value(
                            url = '', 
                            label = '', )
                        }, )
            )
        else:
            return AnswerDetail(
        )
        """

    def testAnswerDetail(self):
        """Test AnswerDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()