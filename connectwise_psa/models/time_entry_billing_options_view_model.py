# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TimeEntryBillingOptionsViewModel(BaseModel):
    """
    TimeEntryBillingOptionsViewModel
    """ # noqa: E501
    applied_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="appliedHours")
    hourly_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="hourlyRate")
    invoice_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="invoiceHours")
    overage_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="overageRate")
    override_flag: Optional[StrictBool] = Field(default=None, alias="overrideFlag")
    total_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalHours")
    __properties: ClassVar[List[str]] = ["appliedHours", "hourlyRate", "invoiceHours", "overageRate", "overrideFlag", "totalHours"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TimeEntryBillingOptionsViewModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if overage_rate (nullable) is None
        # and model_fields_set contains the field
        if self.overage_rate is None and "overage_rate" in self.model_fields_set:
            _dict['overageRate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TimeEntryBillingOptionsViewModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in TimeEntryBillingOptionsViewModel) in the input: " + _key)

        _obj = cls.model_validate({
            "appliedHours": obj.get("appliedHours"),
            "hourlyRate": obj.get("hourlyRate"),
            "invoiceHours": obj.get("invoiceHours"),
            "overageRate": obj.get("overageRate"),
            "overrideFlag": obj.get("overrideFlag"),
            "totalHours": obj.get("totalHours")
        })
        return _obj

