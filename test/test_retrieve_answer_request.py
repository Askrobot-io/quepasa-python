# coding: utf-8

"""
    QuePasa RAG SaaS API

    API for RAG retrieval, managing documents, files, and related operations including Telegram integration.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from quepasa.models.retrieve_answer_request import RetrieveAnswerRequest

class TestRetrieveAnswerRequest(unittest.TestCase):
    """RetrieveAnswerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RetrieveAnswerRequest:
        """Test RetrieveAnswerRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RetrieveAnswerRequest`
        """
        model = RetrieveAnswerRequest()
        if include_optional:
            return RetrieveAnswerRequest(
                question = 'What is LLM?',
                domain = 'default',
                llm = 'anthropic:claude-3-5-sonnet-20240620',
                prompt = 'anthropic:claude-3-5-sonnet-20240620',
                answer_prompt_size = 900,
                prompt_total_size = 8110,
                document_relevance_weights = quepasa.models.retrieve_answer_request_document_relevance_weights.retrieveAnswer_request_document_relevance_weights(
                    text = 0.5, 
                    semantic = 0.5, ),
                chunk_relevance_weights = quepasa.models.retrieve_answer_request_document_relevance_weights.retrieveAnswer_request_document_relevance_weights(
                    text = 0.5, 
                    semantic = 0.5, ),
                user_info = quepasa.models.retrieve_answer_request_user_info.retrieveAnswer_request_user_info(
                    id = 'replace-with-some-user-id', )
            )
        else:
            return RetrieveAnswerRequest(
        )
        """

    def testRetrieveAnswerRequest(self):
        """Test RetrieveAnswerRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
