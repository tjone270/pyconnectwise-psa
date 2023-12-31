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
from connectwise_psa.models.company_reference import CompanyReference
from connectwise_psa.models.google_email_setup_reference import GoogleEmailSetupReference
from connectwise_psa.models.imap_setup_reference import ImapSetupReference
from connectwise_psa.models.member_reference import MemberReference
from connectwise_psa.models.office365_email_setup_reference import Office365EmailSetupReference
from connectwise_psa.models.priority_reference import PriorityReference
from connectwise_psa.models.service_item_reference import ServiceItemReference
from connectwise_psa.models.service_source_reference import ServiceSourceReference
from connectwise_psa.models.service_status_reference import ServiceStatusReference
from connectwise_psa.models.service_sub_type_reference import ServiceSubTypeReference
from connectwise_psa.models.service_type_reference import ServiceTypeReference
from connectwise_psa.models.system_department_reference import SystemDepartmentReference
from connectwise_psa.models.system_location_reference import SystemLocationReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EmailConnector(BaseModel):
    """
    EmailConnector
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    add_cc_flag: Optional[StrictBool] = Field(default=None, alias="addCcFlag")
    asio365_email_setup: Optional[Office365EmailSetupReference] = Field(default=None, alias="asio365EmailSetup")
    bcc_email_to: Optional[StrictStr] = Field(default=None, description=" Max length: 250;", alias="bccEmailTo")
    create_contact_flag: Optional[StrictBool] = Field(default=None, alias="createContactFlag")
    default_company: Optional[CompanyReference] = Field(default=None, alias="defaultCompany")
    default_member: Optional[MemberReference] = Field(default=None, alias="defaultMember")
    department: Optional[SystemDepartmentReference] = None
    discard_duplicates_flag: Optional[StrictBool] = Field(default=None, alias="discardDuplicatesFlag")
    email_errors_to: StrictStr = Field(description=" Max length: 50;", alias="emailErrorsTo")
    email_notify_from: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="emailNotifyFrom")
    email_server_type: Optional[StrictStr] = Field(default=None, alias="emailServerType")
    google_email_setup: Optional[GoogleEmailSetupReference] = Field(default=None, alias="googleEmailSetup")
    id: Optional[StrictInt] = None
    imap_setup: Optional[ImapSetupReference] = Field(default=None, alias="imapSetup")
    inbound_ticket_mailbox_id: Optional[StrictStr] = Field(default=None, alias="inboundTicketMailboxId")
    item_override: Optional[ServiceItemReference] = Field(default=None, alias="itemOverride")
    location: Optional[SystemLocationReference] = None
    never_respond_flag: Optional[StrictBool] = Field(default=None, alias="neverRespondFlag")
    no_response_flag: Optional[StrictBool] = Field(default=None, alias="noResponseFlag")
    office365_email_setup: Optional[Office365EmailSetupReference] = Field(default=None, alias="office365EmailSetup")
    post_replies_to_ticket_flag: Optional[StrictBool] = Field(default=None, alias="postRepliesToTicketFlag")
    priority_override: Optional[PriorityReference] = Field(default=None, alias="priorityOverride")
    response_email_for_existing: Optional[StrictStr] = Field(default=None, alias="responseEmailForExisting")
    response_email_for_new: Optional[StrictStr] = Field(default=None, alias="responseEmailForNew")
    service_board: Optional[BoardReference] = Field(default=None, alias="serviceBoard")
    set_email_to_default_contact_flag: Optional[StrictBool] = Field(default=None, alias="setEmailToDefaultContactFlag")
    source_override: Optional[ServiceSourceReference] = Field(default=None, alias="sourceOverride")
    status_override: Optional[ServiceStatusReference] = Field(default=None, alias="statusOverride")
    sub_type_override: Optional[ServiceSubTypeReference] = Field(default=None, alias="subTypeOverride")
    type_override: Optional[ServiceTypeReference] = Field(default=None, alias="typeOverride")
    use_email_message_id_flag: Optional[StrictBool] = Field(default=None, alias="useEmailMessageIdFlag")
    __properties: ClassVar[List[str]] = ["_info", "addCcFlag", "asio365EmailSetup", "bccEmailTo", "createContactFlag", "defaultCompany", "defaultMember", "department", "discardDuplicatesFlag", "emailErrorsTo", "emailNotifyFrom", "emailServerType", "googleEmailSetup", "id", "imapSetup", "inboundTicketMailboxId", "itemOverride", "location", "neverRespondFlag", "noResponseFlag", "office365EmailSetup", "postRepliesToTicketFlag", "priorityOverride", "responseEmailForExisting", "responseEmailForNew", "serviceBoard", "setEmailToDefaultContactFlag", "sourceOverride", "statusOverride", "subTypeOverride", "typeOverride", "useEmailMessageIdFlag"]

    @field_validator('email_server_type')
    def email_server_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('IMAP', 'Office365', 'Google', 'Asio365'):
            raise ValueError("must be one of enum values ('IMAP', 'Office365', 'Google', 'Asio365')")
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
        """Create an instance of EmailConnector from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of asio365_email_setup
        if self.asio365_email_setup:
            _dict['asio365EmailSetup'] = self.asio365_email_setup.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_company
        if self.default_company:
            _dict['defaultCompany'] = self.default_company.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_member
        if self.default_member:
            _dict['defaultMember'] = self.default_member.to_dict()
        # override the default output from pydantic by calling `to_dict()` of department
        if self.department:
            _dict['department'] = self.department.to_dict()
        # override the default output from pydantic by calling `to_dict()` of google_email_setup
        if self.google_email_setup:
            _dict['googleEmailSetup'] = self.google_email_setup.to_dict()
        # override the default output from pydantic by calling `to_dict()` of imap_setup
        if self.imap_setup:
            _dict['imapSetup'] = self.imap_setup.to_dict()
        # override the default output from pydantic by calling `to_dict()` of item_override
        if self.item_override:
            _dict['itemOverride'] = self.item_override.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of office365_email_setup
        if self.office365_email_setup:
            _dict['office365EmailSetup'] = self.office365_email_setup.to_dict()
        # override the default output from pydantic by calling `to_dict()` of priority_override
        if self.priority_override:
            _dict['priorityOverride'] = self.priority_override.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_board
        if self.service_board:
            _dict['serviceBoard'] = self.service_board.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source_override
        if self.source_override:
            _dict['sourceOverride'] = self.source_override.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status_override
        if self.status_override:
            _dict['statusOverride'] = self.status_override.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sub_type_override
        if self.sub_type_override:
            _dict['subTypeOverride'] = self.sub_type_override.to_dict()
        # override the default output from pydantic by calling `to_dict()` of type_override
        if self.type_override:
            _dict['typeOverride'] = self.type_override.to_dict()
        # set to None if add_cc_flag (nullable) is None
        # and model_fields_set contains the field
        if self.add_cc_flag is None and "add_cc_flag" in self.model_fields_set:
            _dict['addCcFlag'] = None

        # set to None if create_contact_flag (nullable) is None
        # and model_fields_set contains the field
        if self.create_contact_flag is None and "create_contact_flag" in self.model_fields_set:
            _dict['createContactFlag'] = None

        # set to None if discard_duplicates_flag (nullable) is None
        # and model_fields_set contains the field
        if self.discard_duplicates_flag is None and "discard_duplicates_flag" in self.model_fields_set:
            _dict['discardDuplicatesFlag'] = None

        # set to None if email_server_type (nullable) is None
        # and model_fields_set contains the field
        if self.email_server_type is None and "email_server_type" in self.model_fields_set:
            _dict['emailServerType'] = None

        # set to None if never_respond_flag (nullable) is None
        # and model_fields_set contains the field
        if self.never_respond_flag is None and "never_respond_flag" in self.model_fields_set:
            _dict['neverRespondFlag'] = None

        # set to None if no_response_flag (nullable) is None
        # and model_fields_set contains the field
        if self.no_response_flag is None and "no_response_flag" in self.model_fields_set:
            _dict['noResponseFlag'] = None

        # set to None if post_replies_to_ticket_flag (nullable) is None
        # and model_fields_set contains the field
        if self.post_replies_to_ticket_flag is None and "post_replies_to_ticket_flag" in self.model_fields_set:
            _dict['postRepliesToTicketFlag'] = None

        # set to None if set_email_to_default_contact_flag (nullable) is None
        # and model_fields_set contains the field
        if self.set_email_to_default_contact_flag is None and "set_email_to_default_contact_flag" in self.model_fields_set:
            _dict['setEmailToDefaultContactFlag'] = None

        # set to None if use_email_message_id_flag (nullable) is None
        # and model_fields_set contains the field
        if self.use_email_message_id_flag is None and "use_email_message_id_flag" in self.model_fields_set:
            _dict['useEmailMessageIdFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EmailConnector from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in EmailConnector) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "addCcFlag": obj.get("addCcFlag"),
            "asio365EmailSetup": Office365EmailSetupReference.from_dict(obj.get("asio365EmailSetup")) if obj.get("asio365EmailSetup") is not None else None,
            "bccEmailTo": obj.get("bccEmailTo"),
            "createContactFlag": obj.get("createContactFlag"),
            "defaultCompany": CompanyReference.from_dict(obj.get("defaultCompany")) if obj.get("defaultCompany") is not None else None,
            "defaultMember": MemberReference.from_dict(obj.get("defaultMember")) if obj.get("defaultMember") is not None else None,
            "department": SystemDepartmentReference.from_dict(obj.get("department")) if obj.get("department") is not None else None,
            "discardDuplicatesFlag": obj.get("discardDuplicatesFlag"),
            "emailErrorsTo": obj.get("emailErrorsTo"),
            "emailNotifyFrom": obj.get("emailNotifyFrom"),
            "emailServerType": obj.get("emailServerType"),
            "googleEmailSetup": GoogleEmailSetupReference.from_dict(obj.get("googleEmailSetup")) if obj.get("googleEmailSetup") is not None else None,
            "id": obj.get("id"),
            "imapSetup": ImapSetupReference.from_dict(obj.get("imapSetup")) if obj.get("imapSetup") is not None else None,
            "inboundTicketMailboxId": obj.get("inboundTicketMailboxId"),
            "itemOverride": ServiceItemReference.from_dict(obj.get("itemOverride")) if obj.get("itemOverride") is not None else None,
            "location": SystemLocationReference.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "neverRespondFlag": obj.get("neverRespondFlag"),
            "noResponseFlag": obj.get("noResponseFlag"),
            "office365EmailSetup": Office365EmailSetupReference.from_dict(obj.get("office365EmailSetup")) if obj.get("office365EmailSetup") is not None else None,
            "postRepliesToTicketFlag": obj.get("postRepliesToTicketFlag"),
            "priorityOverride": PriorityReference.from_dict(obj.get("priorityOverride")) if obj.get("priorityOverride") is not None else None,
            "responseEmailForExisting": obj.get("responseEmailForExisting"),
            "responseEmailForNew": obj.get("responseEmailForNew"),
            "serviceBoard": BoardReference.from_dict(obj.get("serviceBoard")) if obj.get("serviceBoard") is not None else None,
            "setEmailToDefaultContactFlag": obj.get("setEmailToDefaultContactFlag"),
            "sourceOverride": ServiceSourceReference.from_dict(obj.get("sourceOverride")) if obj.get("sourceOverride") is not None else None,
            "statusOverride": ServiceStatusReference.from_dict(obj.get("statusOverride")) if obj.get("statusOverride") is not None else None,
            "subTypeOverride": ServiceSubTypeReference.from_dict(obj.get("subTypeOverride")) if obj.get("subTypeOverride") is not None else None,
            "typeOverride": ServiceTypeReference.from_dict(obj.get("typeOverride")) if obj.get("typeOverride") is not None else None,
            "useEmailMessageIdFlag": obj.get("useEmailMessageIdFlag")
        })
        return _obj


