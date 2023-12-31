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
from connectwise_psa.models.activity_type_reference import ActivityTypeReference
from connectwise_psa.models.member_reference import MemberReference
from connectwise_psa.models.opportunity_status_reference import OpportunityStatusReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PortalConfigurationOpportunitySetup(BaseModel):
    """
    PortalConfigurationOpportunitySetup
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    acceptance_change_status_flag: Optional[StrictBool] = Field(default=None, alias="acceptanceChangeStatusFlag")
    acceptance_create_activity_flag: Optional[StrictBool] = Field(default=None, alias="acceptanceCreateActivityFlag")
    acceptance_email_activity_type: Optional[ActivityTypeReference] = Field(default=None, alias="acceptanceEmailActivityType")
    acceptance_email_assigned_by_member: Optional[MemberReference] = Field(default=None, alias="acceptanceEmailAssignedByMember")
    acceptance_email_body: Optional[StrictStr] = Field(default=None, alias="acceptanceEmailBody")
    acceptance_email_from_first_name: Optional[StrictStr] = Field(default=None, alias="acceptanceEmailFromFirstName")
    acceptance_email_from_last_name: Optional[StrictStr] = Field(default=None, alias="acceptanceEmailFromLastName")
    acceptance_email_subject: Optional[StrictStr] = Field(default=None, alias="acceptanceEmailSubject")
    acceptance_from_email: Optional[StrictStr] = Field(default=None, description="Gets or sets             required when acceptanceSendEmailFlag is true.", alias="acceptanceFromEmail")
    acceptance_opportunity_status: Optional[OpportunityStatusReference] = Field(default=None, alias="acceptanceOpportunityStatus")
    acceptance_send_email_flag: Optional[StrictBool] = Field(default=None, alias="acceptanceSendEmailFlag")
    add_all_opportunity_statuses: Optional[StrictBool] = Field(default=None, alias="addAllOpportunityStatuses")
    add_all_opportunity_types: Optional[StrictBool] = Field(default=None, alias="addAllOpportunityTypes")
    confirmation_email_body: Optional[StrictStr] = Field(default=None, alias="confirmationEmailBody")
    confirmation_email_from_first_name: Optional[StrictStr] = Field(default=None, alias="confirmationEmailFromFirstName")
    confirmation_email_from_last_name: Optional[StrictStr] = Field(default=None, alias="confirmationEmailFromLastName")
    confirmation_email_subject: Optional[StrictStr] = Field(default=None, alias="confirmationEmailSubject")
    confirmation_email_use_default_company_email_address_flag: Optional[StrictBool] = Field(default=None, alias="confirmationEmailUseDefaultCompanyEmailAddressFlag")
    confirmation_from_email: Optional[StrictStr] = Field(default=None, description="Gets or sets             required when confirmationSendEmailFlag is true.", alias="confirmationFromEmail")
    confirmation_send_email_flag: Optional[StrictBool] = Field(default=None, alias="confirmationSendEmailFlag")
    id: Optional[StrictInt] = None
    opportunity_status_rec_ids: Optional[List[StrictInt]] = Field(default=None, alias="opportunityStatusRecIDs")
    opportunity_type_rec_ids: Optional[List[StrictInt]] = Field(default=None, alias="opportunityTypeRecIDs")
    rejection_change_status_flag: Optional[StrictBool] = Field(default=None, alias="rejectionChangeStatusFlag")
    rejection_create_activity_flag: Optional[StrictBool] = Field(default=None, alias="rejectionCreateActivityFlag")
    rejection_email_activity_type: Optional[ActivityTypeReference] = Field(default=None, alias="rejectionEmailActivityType")
    rejection_email_assigned_by_member: Optional[MemberReference] = Field(default=None, alias="rejectionEmailAssignedByMember")
    rejection_email_body: Optional[StrictStr] = Field(default=None, alias="rejectionEmailBody")
    rejection_email_from_first_name: Optional[StrictStr] = Field(default=None, alias="rejectionEmailFromFirstName")
    rejection_email_from_last_name: Optional[StrictStr] = Field(default=None, alias="rejectionEmailFromLastName")
    rejection_email_subject: Optional[StrictStr] = Field(default=None, alias="rejectionEmailSubject")
    rejection_from_email: Optional[StrictStr] = Field(default=None, description="Gets or sets             required when rejectionSendEmailFlag is true.", alias="rejectionFromEmail")
    rejection_opportunity_status: Optional[OpportunityStatusReference] = Field(default=None, alias="rejectionOpportunityStatus")
    rejection_send_email_flag: Optional[StrictBool] = Field(default=None, alias="rejectionSendEmailFlag")
    remove_all_opportunity_statuses: Optional[StrictBool] = Field(default=None, alias="removeAllOpportunityStatuses")
    remove_all_opportunity_types: Optional[StrictBool] = Field(default=None, alias="removeAllOpportunityTypes")
    restrict_view_by_opportunity_status_flag: Optional[StrictBool] = Field(default=None, alias="restrictViewByOpportunityStatusFlag")
    restrict_view_by_opportunity_type_flag: Optional[StrictBool] = Field(default=None, alias="restrictViewByOpportunityTypeFlag")
    __properties: ClassVar[List[str]] = ["_info", "acceptanceChangeStatusFlag", "acceptanceCreateActivityFlag", "acceptanceEmailActivityType", "acceptanceEmailAssignedByMember", "acceptanceEmailBody", "acceptanceEmailFromFirstName", "acceptanceEmailFromLastName", "acceptanceEmailSubject", "acceptanceFromEmail", "acceptanceOpportunityStatus", "acceptanceSendEmailFlag", "addAllOpportunityStatuses", "addAllOpportunityTypes", "confirmationEmailBody", "confirmationEmailFromFirstName", "confirmationEmailFromLastName", "confirmationEmailSubject", "confirmationEmailUseDefaultCompanyEmailAddressFlag", "confirmationFromEmail", "confirmationSendEmailFlag", "id", "opportunityStatusRecIDs", "opportunityTypeRecIDs", "rejectionChangeStatusFlag", "rejectionCreateActivityFlag", "rejectionEmailActivityType", "rejectionEmailAssignedByMember", "rejectionEmailBody", "rejectionEmailFromFirstName", "rejectionEmailFromLastName", "rejectionEmailSubject", "rejectionFromEmail", "rejectionOpportunityStatus", "rejectionSendEmailFlag", "removeAllOpportunityStatuses", "removeAllOpportunityTypes", "restrictViewByOpportunityStatusFlag", "restrictViewByOpportunityTypeFlag"]

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
        """Create an instance of PortalConfigurationOpportunitySetup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of acceptance_email_activity_type
        if self.acceptance_email_activity_type:
            _dict['acceptanceEmailActivityType'] = self.acceptance_email_activity_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of acceptance_email_assigned_by_member
        if self.acceptance_email_assigned_by_member:
            _dict['acceptanceEmailAssignedByMember'] = self.acceptance_email_assigned_by_member.to_dict()
        # override the default output from pydantic by calling `to_dict()` of acceptance_opportunity_status
        if self.acceptance_opportunity_status:
            _dict['acceptanceOpportunityStatus'] = self.acceptance_opportunity_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rejection_email_activity_type
        if self.rejection_email_activity_type:
            _dict['rejectionEmailActivityType'] = self.rejection_email_activity_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rejection_email_assigned_by_member
        if self.rejection_email_assigned_by_member:
            _dict['rejectionEmailAssignedByMember'] = self.rejection_email_assigned_by_member.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rejection_opportunity_status
        if self.rejection_opportunity_status:
            _dict['rejectionOpportunityStatus'] = self.rejection_opportunity_status.to_dict()
        # set to None if acceptance_change_status_flag (nullable) is None
        # and model_fields_set contains the field
        if self.acceptance_change_status_flag is None and "acceptance_change_status_flag" in self.model_fields_set:
            _dict['acceptanceChangeStatusFlag'] = None

        # set to None if acceptance_create_activity_flag (nullable) is None
        # and model_fields_set contains the field
        if self.acceptance_create_activity_flag is None and "acceptance_create_activity_flag" in self.model_fields_set:
            _dict['acceptanceCreateActivityFlag'] = None

        # set to None if acceptance_send_email_flag (nullable) is None
        # and model_fields_set contains the field
        if self.acceptance_send_email_flag is None and "acceptance_send_email_flag" in self.model_fields_set:
            _dict['acceptanceSendEmailFlag'] = None

        # set to None if add_all_opportunity_statuses (nullable) is None
        # and model_fields_set contains the field
        if self.add_all_opportunity_statuses is None and "add_all_opportunity_statuses" in self.model_fields_set:
            _dict['addAllOpportunityStatuses'] = None

        # set to None if add_all_opportunity_types (nullable) is None
        # and model_fields_set contains the field
        if self.add_all_opportunity_types is None and "add_all_opportunity_types" in self.model_fields_set:
            _dict['addAllOpportunityTypes'] = None

        # set to None if confirmation_email_use_default_company_email_address_flag (nullable) is None
        # and model_fields_set contains the field
        if self.confirmation_email_use_default_company_email_address_flag is None and "confirmation_email_use_default_company_email_address_flag" in self.model_fields_set:
            _dict['confirmationEmailUseDefaultCompanyEmailAddressFlag'] = None

        # set to None if confirmation_send_email_flag (nullable) is None
        # and model_fields_set contains the field
        if self.confirmation_send_email_flag is None and "confirmation_send_email_flag" in self.model_fields_set:
            _dict['confirmationSendEmailFlag'] = None

        # set to None if rejection_change_status_flag (nullable) is None
        # and model_fields_set contains the field
        if self.rejection_change_status_flag is None and "rejection_change_status_flag" in self.model_fields_set:
            _dict['rejectionChangeStatusFlag'] = None

        # set to None if rejection_create_activity_flag (nullable) is None
        # and model_fields_set contains the field
        if self.rejection_create_activity_flag is None and "rejection_create_activity_flag" in self.model_fields_set:
            _dict['rejectionCreateActivityFlag'] = None

        # set to None if rejection_send_email_flag (nullable) is None
        # and model_fields_set contains the field
        if self.rejection_send_email_flag is None and "rejection_send_email_flag" in self.model_fields_set:
            _dict['rejectionSendEmailFlag'] = None

        # set to None if remove_all_opportunity_statuses (nullable) is None
        # and model_fields_set contains the field
        if self.remove_all_opportunity_statuses is None and "remove_all_opportunity_statuses" in self.model_fields_set:
            _dict['removeAllOpportunityStatuses'] = None

        # set to None if remove_all_opportunity_types (nullable) is None
        # and model_fields_set contains the field
        if self.remove_all_opportunity_types is None and "remove_all_opportunity_types" in self.model_fields_set:
            _dict['removeAllOpportunityTypes'] = None

        # set to None if restrict_view_by_opportunity_status_flag (nullable) is None
        # and model_fields_set contains the field
        if self.restrict_view_by_opportunity_status_flag is None and "restrict_view_by_opportunity_status_flag" in self.model_fields_set:
            _dict['restrictViewByOpportunityStatusFlag'] = None

        # set to None if restrict_view_by_opportunity_type_flag (nullable) is None
        # and model_fields_set contains the field
        if self.restrict_view_by_opportunity_type_flag is None and "restrict_view_by_opportunity_type_flag" in self.model_fields_set:
            _dict['restrictViewByOpportunityTypeFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PortalConfigurationOpportunitySetup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in PortalConfigurationOpportunitySetup) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "acceptanceChangeStatusFlag": obj.get("acceptanceChangeStatusFlag"),
            "acceptanceCreateActivityFlag": obj.get("acceptanceCreateActivityFlag"),
            "acceptanceEmailActivityType": ActivityTypeReference.from_dict(obj.get("acceptanceEmailActivityType")) if obj.get("acceptanceEmailActivityType") is not None else None,
            "acceptanceEmailAssignedByMember": MemberReference.from_dict(obj.get("acceptanceEmailAssignedByMember")) if obj.get("acceptanceEmailAssignedByMember") is not None else None,
            "acceptanceEmailBody": obj.get("acceptanceEmailBody"),
            "acceptanceEmailFromFirstName": obj.get("acceptanceEmailFromFirstName"),
            "acceptanceEmailFromLastName": obj.get("acceptanceEmailFromLastName"),
            "acceptanceEmailSubject": obj.get("acceptanceEmailSubject"),
            "acceptanceFromEmail": obj.get("acceptanceFromEmail"),
            "acceptanceOpportunityStatus": OpportunityStatusReference.from_dict(obj.get("acceptanceOpportunityStatus")) if obj.get("acceptanceOpportunityStatus") is not None else None,
            "acceptanceSendEmailFlag": obj.get("acceptanceSendEmailFlag"),
            "addAllOpportunityStatuses": obj.get("addAllOpportunityStatuses"),
            "addAllOpportunityTypes": obj.get("addAllOpportunityTypes"),
            "confirmationEmailBody": obj.get("confirmationEmailBody"),
            "confirmationEmailFromFirstName": obj.get("confirmationEmailFromFirstName"),
            "confirmationEmailFromLastName": obj.get("confirmationEmailFromLastName"),
            "confirmationEmailSubject": obj.get("confirmationEmailSubject"),
            "confirmationEmailUseDefaultCompanyEmailAddressFlag": obj.get("confirmationEmailUseDefaultCompanyEmailAddressFlag"),
            "confirmationFromEmail": obj.get("confirmationFromEmail"),
            "confirmationSendEmailFlag": obj.get("confirmationSendEmailFlag"),
            "id": obj.get("id"),
            "opportunityStatusRecIDs": obj.get("opportunityStatusRecIDs"),
            "opportunityTypeRecIDs": obj.get("opportunityTypeRecIDs"),
            "rejectionChangeStatusFlag": obj.get("rejectionChangeStatusFlag"),
            "rejectionCreateActivityFlag": obj.get("rejectionCreateActivityFlag"),
            "rejectionEmailActivityType": ActivityTypeReference.from_dict(obj.get("rejectionEmailActivityType")) if obj.get("rejectionEmailActivityType") is not None else None,
            "rejectionEmailAssignedByMember": MemberReference.from_dict(obj.get("rejectionEmailAssignedByMember")) if obj.get("rejectionEmailAssignedByMember") is not None else None,
            "rejectionEmailBody": obj.get("rejectionEmailBody"),
            "rejectionEmailFromFirstName": obj.get("rejectionEmailFromFirstName"),
            "rejectionEmailFromLastName": obj.get("rejectionEmailFromLastName"),
            "rejectionEmailSubject": obj.get("rejectionEmailSubject"),
            "rejectionFromEmail": obj.get("rejectionFromEmail"),
            "rejectionOpportunityStatus": OpportunityStatusReference.from_dict(obj.get("rejectionOpportunityStatus")) if obj.get("rejectionOpportunityStatus") is not None else None,
            "rejectionSendEmailFlag": obj.get("rejectionSendEmailFlag"),
            "removeAllOpportunityStatuses": obj.get("removeAllOpportunityStatuses"),
            "removeAllOpportunityTypes": obj.get("removeAllOpportunityTypes"),
            "restrictViewByOpportunityStatusFlag": obj.get("restrictViewByOpportunityStatusFlag"),
            "restrictViewByOpportunityTypeFlag": obj.get("restrictViewByOpportunityTypeFlag")
        })
        return _obj


