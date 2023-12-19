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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from connectwise_psa.models.portal_configuration_payment_processor_reference import PortalConfigurationPaymentProcessorReference
from connectwise_psa.models.portal_configuration_reference import PortalConfigurationReference
from connectwise_psa.models.system_location_reference import SystemLocationReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PortalConfigurationInvoiceSetup(BaseModel):
    """
    PortalConfigurationInvoiceSetup
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    add_all_statuses: Optional[StrictBool] = Field(default=None, alias="addAllStatuses")
    allow_inv_pmt_flag: Optional[StrictBool] = Field(default=None, alias="allowInvPmtFlag")
    billing_status_ids: Optional[List[StrictInt]] = Field(default=None, alias="billingStatusIds")
    display_inv_pmt_flag: Optional[StrictBool] = Field(default=None, alias="displayInvPmtFlag")
    id: Optional[StrictInt] = None
    location: Optional[SystemLocationReference] = None
    login: Optional[StrictStr] = None
    password: Optional[StrictStr] = None
    payment_processor: Optional[PortalConfigurationPaymentProcessorReference] = Field(default=None, alias="paymentProcessor")
    portal_configuration: Optional[PortalConfigurationReference] = Field(default=None, alias="portalConfiguration")
    remove_all_statuses: Optional[StrictBool] = Field(default=None, alias="removeAllStatuses")
    url_override: Optional[StrictStr] = Field(default=None, alias="urlOverride")
    __properties: ClassVar[List[str]] = ["_info", "addAllStatuses", "allowInvPmtFlag", "billingStatusIds", "displayInvPmtFlag", "id", "location", "login", "password", "paymentProcessor", "portalConfiguration", "removeAllStatuses", "urlOverride"]

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
        """Create an instance of PortalConfigurationInvoiceSetup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_processor
        if self.payment_processor:
            _dict['paymentProcessor'] = self.payment_processor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of portal_configuration
        if self.portal_configuration:
            _dict['portalConfiguration'] = self.portal_configuration.to_dict()
        # set to None if add_all_statuses (nullable) is None
        # and model_fields_set contains the field
        if self.add_all_statuses is None and "add_all_statuses" in self.model_fields_set:
            _dict['addAllStatuses'] = None

        # set to None if allow_inv_pmt_flag (nullable) is None
        # and model_fields_set contains the field
        if self.allow_inv_pmt_flag is None and "allow_inv_pmt_flag" in self.model_fields_set:
            _dict['allowInvPmtFlag'] = None

        # set to None if display_inv_pmt_flag (nullable) is None
        # and model_fields_set contains the field
        if self.display_inv_pmt_flag is None and "display_inv_pmt_flag" in self.model_fields_set:
            _dict['displayInvPmtFlag'] = None

        # set to None if remove_all_statuses (nullable) is None
        # and model_fields_set contains the field
        if self.remove_all_statuses is None and "remove_all_statuses" in self.model_fields_set:
            _dict['removeAllStatuses'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PortalConfigurationInvoiceSetup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in PortalConfigurationInvoiceSetup) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "addAllStatuses": obj.get("addAllStatuses"),
            "allowInvPmtFlag": obj.get("allowInvPmtFlag"),
            "billingStatusIds": obj.get("billingStatusIds"),
            "displayInvPmtFlag": obj.get("displayInvPmtFlag"),
            "id": obj.get("id"),
            "location": SystemLocationReference.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "login": obj.get("login"),
            "password": obj.get("password"),
            "paymentProcessor": PortalConfigurationPaymentProcessorReference.from_dict(obj.get("paymentProcessor")) if obj.get("paymentProcessor") is not None else None,
            "portalConfiguration": PortalConfigurationReference.from_dict(obj.get("portalConfiguration")) if obj.get("portalConfiguration") is not None else None,
            "removeAllStatuses": obj.get("removeAllStatuses"),
            "urlOverride": obj.get("urlOverride")
        })
        return _obj


