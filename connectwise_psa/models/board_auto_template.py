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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator
from pydantic import Field
from connectwise_psa.models.board_reference import BoardReference
from connectwise_psa.models.service_item_reference import ServiceItemReference
from connectwise_psa.models.service_sub_type_reference import ServiceSubTypeReference
from connectwise_psa.models.service_template_reference import ServiceTemplateReference
from connectwise_psa.models.service_type_reference import ServiceTypeReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class BoardAutoTemplate(BaseModel):
    """
    BoardAutoTemplate
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    auto_apply_flag: Optional[StrictBool] = Field(default=None, alias="autoApplyFlag")
    board: Optional[BoardReference] = None
    budget_hours_setting: Optional[StrictStr] = Field(default=None, alias="budgetHoursSetting")
    discussion_setting: Optional[StrictStr] = Field(default=None, alias="discussionSetting")
    documents_setting: Optional[StrictStr] = Field(default=None, alias="documentsSetting")
    finance_information_setting: Optional[StrictStr] = Field(default=None, alias="financeInformationSetting")
    id: Optional[StrictInt] = None
    impact_urgency_setting: Optional[StrictStr] = Field(default=None, alias="impactUrgencySetting")
    internal_analysis_setting: Optional[StrictStr] = Field(default=None, alias="internalAnalysisSetting")
    item: Optional[ServiceItemReference] = None
    resolution_setting: Optional[StrictStr] = Field(default=None, alias="resolutionSetting")
    resources_setting: Optional[StrictStr] = Field(default=None, alias="resourcesSetting")
    send_notes_as_email_setting: Optional[StrictStr] = Field(default=None, alias="sendNotesAsEmailSetting")
    service_template: Optional[ServiceTemplateReference] = Field(default=None, alias="serviceTemplate")
    subtype: Optional[ServiceSubTypeReference] = None
    summary_setting: Optional[StrictStr] = Field(default=None, alias="summarySetting")
    tasks_setting: Optional[StrictStr] = Field(default=None, alias="tasksSetting")
    template_priority_setting: Optional[StrictStr] = Field(default=None, alias="templatePrioritySetting")
    type: Optional[ServiceTypeReference] = None
    __properties: ClassVar[List[str]] = ["_info", "autoApplyFlag", "board", "budgetHoursSetting", "discussionSetting", "documentsSetting", "financeInformationSetting", "id", "impactUrgencySetting", "internalAnalysisSetting", "item", "resolutionSetting", "resourcesSetting", "sendNotesAsEmailSetting", "serviceTemplate", "subtype", "summarySetting", "tasksSetting", "templatePrioritySetting", "type"]

    @field_validator('budget_hours_setting')
    def budget_hours_setting_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Append', 'Overwrite', 'Ignore'):
            raise ValueError("must be one of enum values ('Append', 'Overwrite', 'Ignore')")
        return value

    @field_validator('discussion_setting')
    def discussion_setting_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Append', 'Overwrite', 'Ignore'):
            raise ValueError("must be one of enum values ('Append', 'Overwrite', 'Ignore')")
        return value

    @field_validator('documents_setting')
    def documents_setting_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Append', 'Overwrite', 'Ignore'):
            raise ValueError("must be one of enum values ('Append', 'Overwrite', 'Ignore')")
        return value

    @field_validator('finance_information_setting')
    def finance_information_setting_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Append', 'Overwrite', 'Ignore'):
            raise ValueError("must be one of enum values ('Append', 'Overwrite', 'Ignore')")
        return value

    @field_validator('impact_urgency_setting')
    def impact_urgency_setting_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Append', 'Overwrite', 'Ignore'):
            raise ValueError("must be one of enum values ('Append', 'Overwrite', 'Ignore')")
        return value

    @field_validator('internal_analysis_setting')
    def internal_analysis_setting_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Append', 'Overwrite', 'Ignore'):
            raise ValueError("must be one of enum values ('Append', 'Overwrite', 'Ignore')")
        return value

    @field_validator('resolution_setting')
    def resolution_setting_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Append', 'Overwrite', 'Ignore'):
            raise ValueError("must be one of enum values ('Append', 'Overwrite', 'Ignore')")
        return value

    @field_validator('resources_setting')
    def resources_setting_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Append', 'Overwrite', 'Ignore'):
            raise ValueError("must be one of enum values ('Append', 'Overwrite', 'Ignore')")
        return value

    @field_validator('send_notes_as_email_setting')
    def send_notes_as_email_setting_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Append', 'Overwrite', 'Ignore'):
            raise ValueError("must be one of enum values ('Append', 'Overwrite', 'Ignore')")
        return value

    @field_validator('summary_setting')
    def summary_setting_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Append', 'Overwrite', 'Ignore'):
            raise ValueError("must be one of enum values ('Append', 'Overwrite', 'Ignore')")
        return value

    @field_validator('tasks_setting')
    def tasks_setting_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Append', 'Overwrite', 'Ignore'):
            raise ValueError("must be one of enum values ('Append', 'Overwrite', 'Ignore')")
        return value

    @field_validator('template_priority_setting')
    def template_priority_setting_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Append', 'Overwrite', 'Ignore'):
            raise ValueError("must be one of enum values ('Append', 'Overwrite', 'Ignore')")
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
        """Create an instance of BoardAutoTemplate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of board
        if self.board:
            _dict['board'] = self.board.to_dict()
        # override the default output from pydantic by calling `to_dict()` of item
        if self.item:
            _dict['item'] = self.item.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_template
        if self.service_template:
            _dict['serviceTemplate'] = self.service_template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subtype
        if self.subtype:
            _dict['subtype'] = self.subtype.to_dict()
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        # set to None if auto_apply_flag (nullable) is None
        # and model_fields_set contains the field
        if self.auto_apply_flag is None and "auto_apply_flag" in self.model_fields_set:
            _dict['autoApplyFlag'] = None

        # set to None if budget_hours_setting (nullable) is None
        # and model_fields_set contains the field
        if self.budget_hours_setting is None and "budget_hours_setting" in self.model_fields_set:
            _dict['budgetHoursSetting'] = None

        # set to None if discussion_setting (nullable) is None
        # and model_fields_set contains the field
        if self.discussion_setting is None and "discussion_setting" in self.model_fields_set:
            _dict['discussionSetting'] = None

        # set to None if documents_setting (nullable) is None
        # and model_fields_set contains the field
        if self.documents_setting is None and "documents_setting" in self.model_fields_set:
            _dict['documentsSetting'] = None

        # set to None if finance_information_setting (nullable) is None
        # and model_fields_set contains the field
        if self.finance_information_setting is None and "finance_information_setting" in self.model_fields_set:
            _dict['financeInformationSetting'] = None

        # set to None if impact_urgency_setting (nullable) is None
        # and model_fields_set contains the field
        if self.impact_urgency_setting is None and "impact_urgency_setting" in self.model_fields_set:
            _dict['impactUrgencySetting'] = None

        # set to None if internal_analysis_setting (nullable) is None
        # and model_fields_set contains the field
        if self.internal_analysis_setting is None and "internal_analysis_setting" in self.model_fields_set:
            _dict['internalAnalysisSetting'] = None

        # set to None if resolution_setting (nullable) is None
        # and model_fields_set contains the field
        if self.resolution_setting is None and "resolution_setting" in self.model_fields_set:
            _dict['resolutionSetting'] = None

        # set to None if resources_setting (nullable) is None
        # and model_fields_set contains the field
        if self.resources_setting is None and "resources_setting" in self.model_fields_set:
            _dict['resourcesSetting'] = None

        # set to None if send_notes_as_email_setting (nullable) is None
        # and model_fields_set contains the field
        if self.send_notes_as_email_setting is None and "send_notes_as_email_setting" in self.model_fields_set:
            _dict['sendNotesAsEmailSetting'] = None

        # set to None if summary_setting (nullable) is None
        # and model_fields_set contains the field
        if self.summary_setting is None and "summary_setting" in self.model_fields_set:
            _dict['summarySetting'] = None

        # set to None if tasks_setting (nullable) is None
        # and model_fields_set contains the field
        if self.tasks_setting is None and "tasks_setting" in self.model_fields_set:
            _dict['tasksSetting'] = None

        # set to None if template_priority_setting (nullable) is None
        # and model_fields_set contains the field
        if self.template_priority_setting is None and "template_priority_setting" in self.model_fields_set:
            _dict['templatePrioritySetting'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of BoardAutoTemplate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in BoardAutoTemplate) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "autoApplyFlag": obj.get("autoApplyFlag"),
            "board": BoardReference.from_dict(obj.get("board")) if obj.get("board") is not None else None,
            "budgetHoursSetting": obj.get("budgetHoursSetting"),
            "discussionSetting": obj.get("discussionSetting"),
            "documentsSetting": obj.get("documentsSetting"),
            "financeInformationSetting": obj.get("financeInformationSetting"),
            "id": obj.get("id"),
            "impactUrgencySetting": obj.get("impactUrgencySetting"),
            "internalAnalysisSetting": obj.get("internalAnalysisSetting"),
            "item": ServiceItemReference.from_dict(obj.get("item")) if obj.get("item") is not None else None,
            "resolutionSetting": obj.get("resolutionSetting"),
            "resourcesSetting": obj.get("resourcesSetting"),
            "sendNotesAsEmailSetting": obj.get("sendNotesAsEmailSetting"),
            "serviceTemplate": ServiceTemplateReference.from_dict(obj.get("serviceTemplate")) if obj.get("serviceTemplate") is not None else None,
            "subtype": ServiceSubTypeReference.from_dict(obj.get("subtype")) if obj.get("subtype") is not None else None,
            "summarySetting": obj.get("summarySetting"),
            "tasksSetting": obj.get("tasksSetting"),
            "templatePrioritySetting": obj.get("templatePrioritySetting"),
            "type": ServiceTypeReference.from_dict(obj.get("type")) if obj.get("type") is not None else None
        })
        return _obj

