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
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WorkflowEvent(BaseModel):
    """
    WorkflowEvent
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    event_condition: StrictStr = Field(alias="eventCondition")
    execution_time: Optional[StrictStr] = Field(default=None, description="Defaults to Once when not specified", alias="executionTime")
    frequency_of_execution: Optional[StrictInt] = Field(default=None, description="Required when exectionTimes is set to MultipleTimes or Continuously", alias="frequencyOfExecution")
    frequency_unit: Optional[StrictStr] = Field(default=None, description="Required when exectionTimes is set to MultipleTimes or Continuously", alias="frequencyUnit")
    id: Optional[StrictInt] = None
    max_number_of_execution: Optional[StrictInt] = Field(default=None, description="Required when exectionTimes is set to MultipleTimes", alias="maxNumberOfExecution")
    name: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["_info", "eventCondition", "executionTime", "frequencyOfExecution", "frequencyUnit", "id", "maxNumberOfExecution", "name"]

    @field_validator('execution_time')
    def execution_time_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Once', 'MultipleTimes', 'Continuously'):
            raise ValueError("must be one of enum values ('Once', 'MultipleTimes', 'Continuously')")
        return value

    @field_validator('frequency_unit')
    def frequency_unit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Minutes', 'Hours', 'Days', 'Months'):
            raise ValueError("must be one of enum values ('Minutes', 'Hours', 'Days', 'Months')")
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
        """Create an instance of WorkflowEvent from a JSON string"""
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
        # set to None if execution_time (nullable) is None
        # and model_fields_set contains the field
        if self.execution_time is None and "execution_time" in self.model_fields_set:
            _dict['executionTime'] = None

        # set to None if frequency_of_execution (nullable) is None
        # and model_fields_set contains the field
        if self.frequency_of_execution is None and "frequency_of_execution" in self.model_fields_set:
            _dict['frequencyOfExecution'] = None

        # set to None if frequency_unit (nullable) is None
        # and model_fields_set contains the field
        if self.frequency_unit is None and "frequency_unit" in self.model_fields_set:
            _dict['frequencyUnit'] = None

        # set to None if max_number_of_execution (nullable) is None
        # and model_fields_set contains the field
        if self.max_number_of_execution is None and "max_number_of_execution" in self.model_fields_set:
            _dict['maxNumberOfExecution'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WorkflowEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in WorkflowEvent) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "eventCondition": obj.get("eventCondition"),
            "executionTime": obj.get("executionTime"),
            "frequencyOfExecution": obj.get("frequencyOfExecution"),
            "frequencyUnit": obj.get("frequencyUnit"),
            "id": obj.get("id"),
            "maxNumberOfExecution": obj.get("maxNumberOfExecution"),
            "name": obj.get("name")
        })
        return _obj


