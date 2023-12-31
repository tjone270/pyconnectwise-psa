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
from connectwise_psa.models.system_department_reference import SystemDepartmentReference
from connectwise_psa.models.system_location_reference import SystemLocationReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class BoardInfo(BaseModel):
    """
    BoardInfo
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    all_sort: Optional[StrictStr] = Field(default=None, alias="allSort")
    closed_loop_all_flag: Optional[StrictBool] = Field(default=None, alias="closedLoopAllFlag")
    closed_loop_discussions_flag: Optional[StrictBool] = Field(default=None, alias="closedLoopDiscussionsFlag")
    closed_loop_internal_analysis_flag: Optional[StrictBool] = Field(default=None, alias="closedLoopInternalAnalysisFlag")
    closed_loop_resolution_flag: Optional[StrictBool] = Field(default=None, alias="closedLoopResolutionFlag")
    department: Optional[SystemDepartmentReference] = None
    id: Optional[StrictInt] = None
    inactive_flag: Optional[StrictBool] = Field(default=None, alias="inactiveFlag")
    internal_analysis_sort: Optional[StrictStr] = Field(default=None, alias="internalAnalysisSort")
    location: Optional[SystemLocationReference] = None
    name: Optional[StrictStr] = None
    problem_sort: Optional[StrictStr] = Field(default=None, alias="problemSort")
    project_flag: Optional[StrictBool] = Field(default=None, alias="projectFlag")
    resolution_sort: Optional[StrictStr] = Field(default=None, alias="resolutionSort")
    __properties: ClassVar[List[str]] = ["_info", "allSort", "closedLoopAllFlag", "closedLoopDiscussionsFlag", "closedLoopInternalAnalysisFlag", "closedLoopResolutionFlag", "department", "id", "inactiveFlag", "internalAnalysisSort", "location", "name", "problemSort", "projectFlag", "resolutionSort"]

    @field_validator('all_sort')
    def all_sort_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Ascending', 'Descending'):
            raise ValueError("must be one of enum values ('Ascending', 'Descending')")
        return value

    @field_validator('internal_analysis_sort')
    def internal_analysis_sort_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Ascending', 'Descending'):
            raise ValueError("must be one of enum values ('Ascending', 'Descending')")
        return value

    @field_validator('problem_sort')
    def problem_sort_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Ascending', 'Descending'):
            raise ValueError("must be one of enum values ('Ascending', 'Descending')")
        return value

    @field_validator('resolution_sort')
    def resolution_sort_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Ascending', 'Descending'):
            raise ValueError("must be one of enum values ('Ascending', 'Descending')")
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
        """Create an instance of BoardInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of department
        if self.department:
            _dict['department'] = self.department.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # set to None if all_sort (nullable) is None
        # and model_fields_set contains the field
        if self.all_sort is None and "all_sort" in self.model_fields_set:
            _dict['allSort'] = None

        # set to None if closed_loop_all_flag (nullable) is None
        # and model_fields_set contains the field
        if self.closed_loop_all_flag is None and "closed_loop_all_flag" in self.model_fields_set:
            _dict['closedLoopAllFlag'] = None

        # set to None if closed_loop_discussions_flag (nullable) is None
        # and model_fields_set contains the field
        if self.closed_loop_discussions_flag is None and "closed_loop_discussions_flag" in self.model_fields_set:
            _dict['closedLoopDiscussionsFlag'] = None

        # set to None if closed_loop_internal_analysis_flag (nullable) is None
        # and model_fields_set contains the field
        if self.closed_loop_internal_analysis_flag is None and "closed_loop_internal_analysis_flag" in self.model_fields_set:
            _dict['closedLoopInternalAnalysisFlag'] = None

        # set to None if closed_loop_resolution_flag (nullable) is None
        # and model_fields_set contains the field
        if self.closed_loop_resolution_flag is None and "closed_loop_resolution_flag" in self.model_fields_set:
            _dict['closedLoopResolutionFlag'] = None

        # set to None if inactive_flag (nullable) is None
        # and model_fields_set contains the field
        if self.inactive_flag is None and "inactive_flag" in self.model_fields_set:
            _dict['inactiveFlag'] = None

        # set to None if internal_analysis_sort (nullable) is None
        # and model_fields_set contains the field
        if self.internal_analysis_sort is None and "internal_analysis_sort" in self.model_fields_set:
            _dict['internalAnalysisSort'] = None

        # set to None if problem_sort (nullable) is None
        # and model_fields_set contains the field
        if self.problem_sort is None and "problem_sort" in self.model_fields_set:
            _dict['problemSort'] = None

        # set to None if project_flag (nullable) is None
        # and model_fields_set contains the field
        if self.project_flag is None and "project_flag" in self.model_fields_set:
            _dict['projectFlag'] = None

        # set to None if resolution_sort (nullable) is None
        # and model_fields_set contains the field
        if self.resolution_sort is None and "resolution_sort" in self.model_fields_set:
            _dict['resolutionSort'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of BoardInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in BoardInfo) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "allSort": obj.get("allSort"),
            "closedLoopAllFlag": obj.get("closedLoopAllFlag"),
            "closedLoopDiscussionsFlag": obj.get("closedLoopDiscussionsFlag"),
            "closedLoopInternalAnalysisFlag": obj.get("closedLoopInternalAnalysisFlag"),
            "closedLoopResolutionFlag": obj.get("closedLoopResolutionFlag"),
            "department": SystemDepartmentReference.from_dict(obj.get("department")) if obj.get("department") is not None else None,
            "id": obj.get("id"),
            "inactiveFlag": obj.get("inactiveFlag"),
            "internalAnalysisSort": obj.get("internalAnalysisSort"),
            "location": SystemLocationReference.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "name": obj.get("name"),
            "problemSort": obj.get("problemSort"),
            "projectFlag": obj.get("projectFlag"),
            "resolutionSort": obj.get("resolutionSort")
        })
        return _obj


