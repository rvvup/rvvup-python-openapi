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
import json
from enum import Enum
from typing_extensions import Self


class PaymentSessionStatus(str, Enum):
    """
    The status of the payment session.
    """

    """
    allowed enum values
    """
    CANCELLED = 'CANCELLED'
    DECLINED = 'DECLINED'
    EXPIRED = 'EXPIRED'
    PENDING = 'PENDING'
    REQUIRES_ACTION = 'REQUIRES_ACTION'
    REQUIRES_PAYMENT = 'REQUIRES_PAYMENT'
    SUCCEEDED = 'SUCCEEDED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PaymentSessionStatus from a JSON string"""
        return cls(json.loads(json_str))

