# coding: utf-8

"""
    QuePasa RAG SaaS API

    API for RAG retrieval, managing documents, files, and related operations including Telegram integration.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from quepasa.models.retrieve_answer_request_document_relevance_weights import RetrieveAnswerRequestDocumentRelevanceWeights
from quepasa.models.retrieve_answer_request_relevance_weights import RetrieveAnswerRequestRelevanceWeights
from quepasa.models.retrieve_answer_request_user_info import RetrieveAnswerRequestUserInfo
from typing import Optional, Set
from typing_extensions import Self

class RetrieveChunksRequest(BaseModel):
    """
    RetrieveChunksRequest
    """ # noqa: E501
    question: Optional[StrictStr] = Field(default=None, description="Natural language query to retrieve or answer.")
    domain: Optional[StrictStr] = Field(default=None, description="The name of a group of documents.")
    kind: Optional[StrictStr] = Field(default=None, description="(Experimental) Specifies the type of chunk. Can be \"text\" for raw text chunks, \"summary\" for chunks that are summaries of raw text, or \"all\" to include both types.")
    relevance_weights: Optional[RetrieveAnswerRequestRelevanceWeights] = None
    document_relevance_weights: Optional[RetrieveAnswerRequestDocumentRelevanceWeights] = None
    chunk_relevance_weights: Optional[RetrieveAnswerRequestDocumentRelevanceWeights] = None
    reranker_prompt: Optional[StrictStr] = Field(default=None, description="A prompt template used by the reranking model to prioritize and reorder both documents and chunks based on their relevance to a query. This prompt guides the model in assessing the importance of each document and refining the ranking output. ")
    document_reranker_prompt: Optional[StrictStr] = Field(default=None, description="A prompt template used by the reranking model to prioritize and reorder documents based on their relevance to a query. This prompt guides the model in assessing the importance of each document and refining the ranking output. ")
    chunk_reranker_prompt: Optional[StrictStr] = Field(default=None, description="A prompt template used by the reranking model to prioritize and reorder chunks based on their relevance to a query. This prompt guides the model in assessing the importance of each document and refining the ranking output. ")
    user_info: Optional[RetrieveAnswerRequestUserInfo] = None
    __properties: ClassVar[List[str]] = ["question", "domain", "kind", "relevance_weights", "document_relevance_weights", "chunk_relevance_weights", "reranker_prompt", "document_reranker_prompt", "chunk_reranker_prompt", "user_info"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RetrieveChunksRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of relevance_weights
        if self.relevance_weights:
            _dict['relevance_weights'] = self.relevance_weights.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document_relevance_weights
        if self.document_relevance_weights:
            _dict['document_relevance_weights'] = self.document_relevance_weights.to_dict()
        # override the default output from pydantic by calling `to_dict()` of chunk_relevance_weights
        if self.chunk_relevance_weights:
            _dict['chunk_relevance_weights'] = self.chunk_relevance_weights.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_info
        if self.user_info:
            _dict['user_info'] = self.user_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RetrieveChunksRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "question": obj.get("question"),
            "domain": obj.get("domain"),
            "kind": obj.get("kind"),
            "relevance_weights": RetrieveAnswerRequestRelevanceWeights.from_dict(obj["relevance_weights"]) if obj.get("relevance_weights") is not None else None,
            "document_relevance_weights": RetrieveAnswerRequestDocumentRelevanceWeights.from_dict(obj["document_relevance_weights"]) if obj.get("document_relevance_weights") is not None else None,
            "chunk_relevance_weights": RetrieveAnswerRequestDocumentRelevanceWeights.from_dict(obj["chunk_relevance_weights"]) if obj.get("chunk_relevance_weights") is not None else None,
            "reranker_prompt": obj.get("reranker_prompt"),
            "document_reranker_prompt": obj.get("document_reranker_prompt"),
            "chunk_reranker_prompt": obj.get("chunk_reranker_prompt"),
            "user_info": RetrieveAnswerRequestUserInfo.from_dict(obj["user_info"]) if obj.get("user_info") is not None else None
        })
        return _obj


