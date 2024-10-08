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
from quepasa.models.answer_detail_data_labeled_links_value import AnswerDetailDataLabeledLinksValue
from quepasa.models.answer_detail_data_links_value import AnswerDetailDataLinksValue
from typing import Optional, Set
from typing_extensions import Self

class AnswerDetailData(BaseModel):
    """
    AnswerDetailData
    """ # noqa: E501
    answer: Optional[StrictStr] = Field(default=None, description="The answer generated in response to the query.")
    links: Optional[Dict[str, AnswerDetailDataLinksValue]] = Field(default=None, description="A list of references used in the generated answer.")
    markdown: Optional[StrictStr] = Field(default=None, description="Answer formatted in Markdown, with links.")
    labeled_links: Optional[Dict[str, AnswerDetailDataLabeledLinksValue]] = Field(default=None, description="References in Markdown format.")
    __properties: ClassVar[List[str]] = ["answer", "links", "markdown", "labeled_links"]

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
        """Create an instance of AnswerDetailData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in links (dict)
        _field_dict = {}
        if self.links:
            for _key_links in self.links:
                if self.links[_key_links]:
                    _field_dict[_key_links] = self.links[_key_links].to_dict()
            _dict['links'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in labeled_links (dict)
        _field_dict = {}
        if self.labeled_links:
            for _key_labeled_links in self.labeled_links:
                if self.labeled_links[_key_labeled_links]:
                    _field_dict[_key_labeled_links] = self.labeled_links[_key_labeled_links].to_dict()
            _dict['labeled_links'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AnswerDetailData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "answer": obj.get("answer"),
            "links": dict(
                (_k, AnswerDetailDataLinksValue.from_dict(_v))
                for _k, _v in obj["links"].items()
            )
            if obj.get("links") is not None
            else None,
            "markdown": obj.get("markdown"),
            "labeled_links": dict(
                (_k, AnswerDetailDataLabeledLinksValue.from_dict(_v))
                for _k, _v in obj["labeled_links"].items()
            )
            if obj.get("labeled_links") is not None
            else None
        })
        return _obj


