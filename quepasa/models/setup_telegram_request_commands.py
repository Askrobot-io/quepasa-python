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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from quepasa.models.setup_telegram_request_commands_ask import SetupTelegramRequestCommandsAsk
from quepasa.models.setup_telegram_request_commands_start import SetupTelegramRequestCommandsStart
from typing import Optional, Set
from typing_extensions import Self

class SetupTelegramRequestCommands(BaseModel):
    """
    Telegram bot commands.
    """ # noqa: E501
    start: Optional[SetupTelegramRequestCommandsStart] = None
    ask: Optional[SetupTelegramRequestCommandsAsk] = None
    __properties: ClassVar[List[str]] = ["start", "ask"]

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
        """Create an instance of SetupTelegramRequestCommands from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of start
        if self.start:
            _dict['start'] = self.start.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ask
        if self.ask:
            _dict['ask'] = self.ask.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SetupTelegramRequestCommands from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "start": SetupTelegramRequestCommandsStart.from_dict(obj["start"]) if obj.get("start") is not None else None,
            "ask": SetupTelegramRequestCommandsAsk.from_dict(obj["ask"]) if obj.get("ask") is not None else None
        })
        return _obj


