# coding: utf-8

"""
    Rvvup API

    Rvvup Public API

    The version of the OpenAPI document: 2024-03-01
    Contact: info@rvvup.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Address(BaseModel):
    """
    Address
    """ # noqa: E501
    city: StrictStr = Field(description="City.")
    company: Optional[StrictStr] = Field(default=None, description="Company name.")
    country_code: StrictStr = Field(description="Two letter ISO 3166-1 alpha-2 country code.", alias="countryCode")
    line1: StrictStr = Field(description="Address line 1.")
    line2: Optional[StrictStr] = Field(default=None, description="Address line 2.")
    name: StrictStr = Field(description="Name.")
    phone_number: Optional[StrictStr] = Field(default=None, description="Phone number.", alias="phoneNumber")
    postcode: StrictStr = Field(description="Postcode.")
    state: Optional[StrictStr] = Field(default=None, description="State.")
    __properties: ClassVar[List[str]] = ["city", "company", "countryCode", "line1", "line2", "name", "phoneNumber", "postcode", "state"]

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
        """Create an instance of Address from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Address from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "city": obj.get("city"),
            "company": obj.get("company"),
            "countryCode": obj.get("countryCode"),
            "line1": obj.get("line1"),
            "line2": obj.get("line2"),
            "name": obj.get("name"),
            "phoneNumber": obj.get("phoneNumber"),
            "postcode": obj.get("postcode"),
            "state": obj.get("state")
        })
        return _obj


