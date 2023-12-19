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
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from connectwise_psa.models.agreement_reference import AgreementReference
from connectwise_psa.models.agreement_type_reference import AgreementTypeReference
from connectwise_psa.models.board_reference import BoardReference
from connectwise_psa.models.company_reference import CompanyReference
from connectwise_psa.models.iv_item_reference import IvItemReference
from connectwise_psa.models.member_reference import MemberReference
from connectwise_psa.models.product_category_reference import ProductCategoryReference
from connectwise_psa.models.product_sub_category_reference import ProductSubCategoryReference
from connectwise_psa.models.project_board_reference import ProjectBoardReference
from connectwise_psa.models.project_reference import ProjectReference
from connectwise_psa.models.project_type_reference import ProjectTypeReference
from connectwise_psa.models.service_type_reference import ServiceTypeReference
from connectwise_psa.models.site_reference import SiteReference
from connectwise_psa.models.system_department_reference import SystemDepartmentReference
from connectwise_psa.models.system_location_reference import SystemLocationReference
from connectwise_psa.models.ticket_reference import TicketReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Commission(BaseModel):
    """
    Commission
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    agreement: Optional[AgreementReference] = None
    agreement_type: Optional[AgreementTypeReference] = Field(default=None, alias="agreementType")
    agreements_flag: Optional[StrictBool] = Field(default=None, alias="agreementsFlag")
    billing_method: Optional[StrictStr] = Field(default=None, alias="billingMethod")
    commission_basis: Optional[StrictStr] = Field(default=None, alias="commissionBasis")
    commission_percent: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="commissionPercent")
    company: Optional[CompanyReference] = None
    date_end: Optional[datetime] = Field(default=None, alias="dateEnd")
    date_start: Optional[datetime] = Field(default=None, alias="dateStart")
    department: Optional[SystemDepartmentReference] = None
    id: Optional[StrictInt] = None
    invoice_option: Optional[StrictStr] = Field(default=None, alias="invoiceOption")
    item: Optional[IvItemReference] = None
    location: Optional[SystemLocationReference] = None
    member: Optional[MemberReference] = None
    my_opportunities_flag: Optional[StrictBool] = Field(default=None, alias="myOpportunitiesFlag")
    number_of_months: Optional[StrictInt] = Field(default=None, alias="numberOfMonths")
    product_category: Optional[ProductCategoryReference] = Field(default=None, alias="productCategory")
    product_sub_category: Optional[ProductSubCategoryReference] = Field(default=None, alias="productSubCategory")
    products_flag: Optional[StrictBool] = Field(default=None, alias="productsFlag")
    project: Optional[ProjectReference] = None
    project_board: Optional[ProjectBoardReference] = Field(default=None, alias="projectBoard")
    project_type: Optional[ProjectTypeReference] = Field(default=None, alias="projectType")
    service_board: Optional[BoardReference] = Field(default=None, alias="serviceBoard")
    service_type: Optional[ServiceTypeReference] = Field(default=None, alias="serviceType")
    services_flag: Optional[StrictBool] = Field(default=None, alias="servicesFlag")
    site: Optional[SiteReference] = None
    territory: Optional[SystemLocationReference] = None
    ticket: Optional[TicketReference] = None
    __properties: ClassVar[List[str]] = ["_info", "agreement", "agreementType", "agreementsFlag", "billingMethod", "commissionBasis", "commissionPercent", "company", "dateEnd", "dateStart", "department", "id", "invoiceOption", "item", "location", "member", "myOpportunitiesFlag", "numberOfMonths", "productCategory", "productSubCategory", "productsFlag", "project", "projectBoard", "projectType", "serviceBoard", "serviceType", "servicesFlag", "site", "territory", "ticket"]

    @field_validator('billing_method')
    def billing_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Agreement', 'CreditMemo', 'DownPayment', 'Miscellaneous', 'Progress', 'Standard'):
            raise ValueError("must be one of enum values ('Agreement', 'CreditMemo', 'DownPayment', 'Miscellaneous', 'Progress', 'Standard')")
        return value

    @field_validator('commission_basis')
    def commission_basis_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('GrossProfit', 'SalesAmount'):
            raise ValueError("must be one of enum values ('GrossProfit', 'SalesAmount')")
        return value

    @field_validator('invoice_option')
    def invoice_option_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('AllInvoices', 'PaidInvoices'):
            raise ValueError("must be one of enum values ('AllInvoices', 'PaidInvoices')")
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
        """Create an instance of Commission from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of agreement_type
        if self.agreement_type:
            _dict['agreementType'] = self.agreement_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of company
        if self.company:
            _dict['company'] = self.company.to_dict()
        # override the default output from pydantic by calling `to_dict()` of department
        if self.department:
            _dict['department'] = self.department.to_dict()
        # override the default output from pydantic by calling `to_dict()` of item
        if self.item:
            _dict['item'] = self.item.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of member
        if self.member:
            _dict['member'] = self.member.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product_category
        if self.product_category:
            _dict['productCategory'] = self.product_category.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product_sub_category
        if self.product_sub_category:
            _dict['productSubCategory'] = self.product_sub_category.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project_board
        if self.project_board:
            _dict['projectBoard'] = self.project_board.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project_type
        if self.project_type:
            _dict['projectType'] = self.project_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_board
        if self.service_board:
            _dict['serviceBoard'] = self.service_board.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_type
        if self.service_type:
            _dict['serviceType'] = self.service_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of site
        if self.site:
            _dict['site'] = self.site.to_dict()
        # override the default output from pydantic by calling `to_dict()` of territory
        if self.territory:
            _dict['territory'] = self.territory.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ticket
        if self.ticket:
            _dict['ticket'] = self.ticket.to_dict()
        # set to None if agreements_flag (nullable) is None
        # and model_fields_set contains the field
        if self.agreements_flag is None and "agreements_flag" in self.model_fields_set:
            _dict['agreementsFlag'] = None

        # set to None if billing_method (nullable) is None
        # and model_fields_set contains the field
        if self.billing_method is None and "billing_method" in self.model_fields_set:
            _dict['billingMethod'] = None

        # set to None if commission_basis (nullable) is None
        # and model_fields_set contains the field
        if self.commission_basis is None and "commission_basis" in self.model_fields_set:
            _dict['commissionBasis'] = None

        # set to None if commission_percent (nullable) is None
        # and model_fields_set contains the field
        if self.commission_percent is None and "commission_percent" in self.model_fields_set:
            _dict['commissionPercent'] = None

        # set to None if invoice_option (nullable) is None
        # and model_fields_set contains the field
        if self.invoice_option is None and "invoice_option" in self.model_fields_set:
            _dict['invoiceOption'] = None

        # set to None if my_opportunities_flag (nullable) is None
        # and model_fields_set contains the field
        if self.my_opportunities_flag is None and "my_opportunities_flag" in self.model_fields_set:
            _dict['myOpportunitiesFlag'] = None

        # set to None if number_of_months (nullable) is None
        # and model_fields_set contains the field
        if self.number_of_months is None and "number_of_months" in self.model_fields_set:
            _dict['numberOfMonths'] = None

        # set to None if products_flag (nullable) is None
        # and model_fields_set contains the field
        if self.products_flag is None and "products_flag" in self.model_fields_set:
            _dict['productsFlag'] = None

        # set to None if services_flag (nullable) is None
        # and model_fields_set contains the field
        if self.services_flag is None and "services_flag" in self.model_fields_set:
            _dict['servicesFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Commission from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Commission) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "agreement": AgreementReference.from_dict(obj.get("agreement")) if obj.get("agreement") is not None else None,
            "agreementType": AgreementTypeReference.from_dict(obj.get("agreementType")) if obj.get("agreementType") is not None else None,
            "agreementsFlag": obj.get("agreementsFlag"),
            "billingMethod": obj.get("billingMethod"),
            "commissionBasis": obj.get("commissionBasis"),
            "commissionPercent": obj.get("commissionPercent"),
            "company": CompanyReference.from_dict(obj.get("company")) if obj.get("company") is not None else None,
            "dateEnd": obj.get("dateEnd"),
            "dateStart": obj.get("dateStart"),
            "department": SystemDepartmentReference.from_dict(obj.get("department")) if obj.get("department") is not None else None,
            "id": obj.get("id"),
            "invoiceOption": obj.get("invoiceOption"),
            "item": IvItemReference.from_dict(obj.get("item")) if obj.get("item") is not None else None,
            "location": SystemLocationReference.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "member": MemberReference.from_dict(obj.get("member")) if obj.get("member") is not None else None,
            "myOpportunitiesFlag": obj.get("myOpportunitiesFlag"),
            "numberOfMonths": obj.get("numberOfMonths"),
            "productCategory": ProductCategoryReference.from_dict(obj.get("productCategory")) if obj.get("productCategory") is not None else None,
            "productSubCategory": ProductSubCategoryReference.from_dict(obj.get("productSubCategory")) if obj.get("productSubCategory") is not None else None,
            "productsFlag": obj.get("productsFlag"),
            "project": ProjectReference.from_dict(obj.get("project")) if obj.get("project") is not None else None,
            "projectBoard": ProjectBoardReference.from_dict(obj.get("projectBoard")) if obj.get("projectBoard") is not None else None,
            "projectType": ProjectTypeReference.from_dict(obj.get("projectType")) if obj.get("projectType") is not None else None,
            "serviceBoard": BoardReference.from_dict(obj.get("serviceBoard")) if obj.get("serviceBoard") is not None else None,
            "serviceType": ServiceTypeReference.from_dict(obj.get("serviceType")) if obj.get("serviceType") is not None else None,
            "servicesFlag": obj.get("servicesFlag"),
            "site": SiteReference.from_dict(obj.get("site")) if obj.get("site") is not None else None,
            "territory": SystemLocationReference.from_dict(obj.get("territory")) if obj.get("territory") is not None else None,
            "ticket": TicketReference.from_dict(obj.get("ticket")) if obj.get("ticket") is not None else None
        })
        return _obj


