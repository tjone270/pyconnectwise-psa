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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from connectwise_psa.models.agreement_reference import AgreementReference
from connectwise_psa.models.owner_level_reference import OwnerLevelReference
from connectwise_psa.models.work_role_reference import WorkRoleReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AgreementWorkRole(BaseModel):
    """
    AgreementWorkRole
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    agreement: Optional[AgreementReference] = None
    agreement_id: Optional[StrictInt] = Field(default=None, alias="agreementId")
    effective_date: Optional[datetime] = Field(default=None, alias="effectiveDate")
    ending_date: Optional[datetime] = Field(default=None, alias="endingDate")
    id: Optional[StrictInt] = None
    limit_to: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="limitTo")
    location: Optional[OwnerLevelReference] = None
    location_id: Optional[StrictInt] = Field(default=None, alias="locationId")
    rate: Optional[Union[StrictFloat, StrictInt]] = None
    rate_type: Optional[StrictStr] = Field(alias="rateType")
    work_role: Optional[WorkRoleReference] = Field(default=None, alias="workRole")
    __properties: ClassVar[List[str]] = ["_info", "agreement", "agreementId", "effectiveDate", "endingDate", "id", "limitTo", "location", "locationId", "rate", "rateType", "workRole"]

    @field_validator('rate_type')
    def rate_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('AdjAmount', 'Custom', 'Multiplier'):
            raise ValueError("must be one of enum values ('AdjAmount', 'Custom', 'Multiplier')")
        return value

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
        """Create an instance of AgreementWorkRole from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of agreement
        if self.agreement:
            _dict['agreement'] = self.agreement.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of work_role
        if self.work_role:
            _dict['workRole'] = self.work_role.to_dict()
        # set to None if agreement_id (nullable) is None
        # and model_fields_set contains the field
        if self.agreement_id is None and "agreement_id" in self.model_fields_set:
            _dict['agreementId'] = None

        # set to None if limit_to (nullable) is None
        # and model_fields_set contains the field
        if self.limit_to is None and "limit_to" in self.model_fields_set:
            _dict['limitTo'] = None

        # set to None if location_id (nullable) is None
        # and model_fields_set contains the field
        if self.location_id is None and "location_id" in self.model_fields_set:
            _dict['locationId'] = None

        # set to None if rate (nullable) is None
        # and model_fields_set contains the field
        if self.rate is None and "rate" in self.model_fields_set:
            _dict['rate'] = None

        # set to None if rate_type (nullable) is None
        # and model_fields_set contains the field
        if self.rate_type is None and "rate_type" in self.model_fields_set:
            _dict['rateType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AgreementWorkRole from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in AgreementWorkRole) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "agreement": AgreementReference.from_dict(obj.get("agreement")) if obj.get("agreement") is not None else None,
            "agreementId": obj.get("agreementId"),
            "effectiveDate": obj.get("effectiveDate"),
            "endingDate": obj.get("endingDate"),
            "id": obj.get("id"),
            "limitTo": obj.get("limitTo"),
            "location": OwnerLevelReference.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "locationId": obj.get("locationId"),
            "rate": obj.get("rate"),
            "rateType": obj.get("rateType"),
            "workRole": WorkRoleReference.from_dict(obj.get("workRole")) if obj.get("workRole") is not None else None
        })
        return _obj


