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
from connectwise_psa.models.team_role_reference import TeamRoleReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Crm(BaseModel):
    """
    Crm
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    account_manager_role: Optional[TeamRoleReference] = Field(default=None, alias="accountManagerRole")
    company_id_generation_flag: Optional[StrictBool] = Field(default=None, alias="companyIdGenerationFlag")
    company_list_count: Optional[StrictInt] = Field(default=None, alias="companyListCount")
    default_year: Optional[StrictBool] = Field(default=None, alias="defaultYear")
    exclude_spaces_flag: Optional[StrictBool] = Field(default=None, alias="excludeSpacesFlag")
    field10_caption: Optional[StrictStr] = Field(default=None, description=" Max length: 25;", alias="field10Caption")
    field1_caption: Optional[StrictStr] = Field(default=None, description=" Max length: 25;", alias="field1Caption")
    field2_caption: Optional[StrictStr] = Field(default=None, description=" Max length: 25;", alias="field2Caption")
    field3_caption: Optional[StrictStr] = Field(default=None, description=" Max length: 25;", alias="field3Caption")
    field4_caption: Optional[StrictStr] = Field(default=None, description=" Max length: 25;", alias="field4Caption")
    field5_caption: Optional[StrictStr] = Field(default=None, description=" Max length: 25;", alias="field5Caption")
    field6_caption: Optional[StrictStr] = Field(default=None, description=" Max length: 25;", alias="field6Caption")
    field7_caption: Optional[StrictStr] = Field(default=None, description=" Max length: 25;", alias="field7Caption")
    field8_caption: Optional[StrictStr] = Field(default=None, description=" Max length: 25;", alias="field8Caption")
    field9_caption: Optional[StrictStr] = Field(default=None, description=" Max length: 25;", alias="field9Caption")
    id: Optional[StrictInt] = None
    lock_probability_flag: Optional[StrictBool] = Field(default=None, alias="lockProbabilityFlag")
    other1_caption: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="other1Caption")
    other2_caption: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="other2Caption")
    primary_rep_caption: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="primaryRepCaption")
    sales_rep_role: Optional[TeamRoleReference] = Field(default=None, alias="salesRepRole")
    secondary_rep_caption: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="secondaryRepCaption")
    technical_contact_role: Optional[TeamRoleReference] = Field(default=None, alias="technicalContactRole")
    __properties: ClassVar[List[str]] = ["_info", "accountManagerRole", "companyIdGenerationFlag", "companyListCount", "defaultYear", "excludeSpacesFlag", "field10Caption", "field1Caption", "field2Caption", "field3Caption", "field4Caption", "field5Caption", "field6Caption", "field7Caption", "field8Caption", "field9Caption", "id", "lockProbabilityFlag", "other1Caption", "other2Caption", "primaryRepCaption", "salesRepRole", "secondaryRepCaption", "technicalContactRole"]

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
        """Create an instance of Crm from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account_manager_role
        if self.account_manager_role:
            _dict['accountManagerRole'] = self.account_manager_role.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sales_rep_role
        if self.sales_rep_role:
            _dict['salesRepRole'] = self.sales_rep_role.to_dict()
        # override the default output from pydantic by calling `to_dict()` of technical_contact_role
        if self.technical_contact_role:
            _dict['technicalContactRole'] = self.technical_contact_role.to_dict()
        # set to None if company_id_generation_flag (nullable) is None
        # and model_fields_set contains the field
        if self.company_id_generation_flag is None and "company_id_generation_flag" in self.model_fields_set:
            _dict['companyIdGenerationFlag'] = None

        # set to None if company_list_count (nullable) is None
        # and model_fields_set contains the field
        if self.company_list_count is None and "company_list_count" in self.model_fields_set:
            _dict['companyListCount'] = None

        # set to None if default_year (nullable) is None
        # and model_fields_set contains the field
        if self.default_year is None and "default_year" in self.model_fields_set:
            _dict['defaultYear'] = None

        # set to None if exclude_spaces_flag (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_spaces_flag is None and "exclude_spaces_flag" in self.model_fields_set:
            _dict['excludeSpacesFlag'] = None

        # set to None if lock_probability_flag (nullable) is None
        # and model_fields_set contains the field
        if self.lock_probability_flag is None and "lock_probability_flag" in self.model_fields_set:
            _dict['lockProbabilityFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Crm from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Crm) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "accountManagerRole": TeamRoleReference.from_dict(obj.get("accountManagerRole")) if obj.get("accountManagerRole") is not None else None,
            "companyIdGenerationFlag": obj.get("companyIdGenerationFlag"),
            "companyListCount": obj.get("companyListCount"),
            "defaultYear": obj.get("defaultYear"),
            "excludeSpacesFlag": obj.get("excludeSpacesFlag"),
            "field10Caption": obj.get("field10Caption"),
            "field1Caption": obj.get("field1Caption"),
            "field2Caption": obj.get("field2Caption"),
            "field3Caption": obj.get("field3Caption"),
            "field4Caption": obj.get("field4Caption"),
            "field5Caption": obj.get("field5Caption"),
            "field6Caption": obj.get("field6Caption"),
            "field7Caption": obj.get("field7Caption"),
            "field8Caption": obj.get("field8Caption"),
            "field9Caption": obj.get("field9Caption"),
            "id": obj.get("id"),
            "lockProbabilityFlag": obj.get("lockProbabilityFlag"),
            "other1Caption": obj.get("other1Caption"),
            "other2Caption": obj.get("other2Caption"),
            "primaryRepCaption": obj.get("primaryRepCaption"),
            "salesRepRole": TeamRoleReference.from_dict(obj.get("salesRepRole")) if obj.get("salesRepRole") is not None else None,
            "secondaryRepCaption": obj.get("secondaryRepCaption"),
            "technicalContactRole": TeamRoleReference.from_dict(obj.get("technicalContactRole")) if obj.get("technicalContactRole") is not None else None
        })
        return _obj


