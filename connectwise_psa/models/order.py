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
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from connectwise_psa.models.billing_terms_reference import BillingTermsReference
from connectwise_psa.models.company_reference import CompanyReference
from connectwise_psa.models.contact_reference import ContactReference
from connectwise_psa.models.currency_reference import CurrencyReference
from connectwise_psa.models.custom_field_value import CustomFieldValue
from connectwise_psa.models.member_reference import MemberReference
from connectwise_psa.models.opportunity_reference import OpportunityReference
from connectwise_psa.models.order_status_reference import OrderStatusReference
from connectwise_psa.models.site_reference import SiteReference
from connectwise_psa.models.system_department_reference import SystemDepartmentReference
from connectwise_psa.models.system_location_reference import SystemLocationReference
from connectwise_psa.models.tax_code_reference import TaxCodeReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Order(BaseModel):
    """
    Order
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    bill_closed_flag: Optional[StrictBool] = Field(default=None, alias="billClosedFlag")
    bill_shipped_flag: Optional[StrictBool] = Field(default=None, alias="billShippedFlag")
    bill_to_company: Optional[CompanyReference] = Field(default=None, alias="billToCompany")
    bill_to_contact: Optional[ContactReference] = Field(default=None, alias="billToContact")
    bill_to_site: Optional[SiteReference] = Field(default=None, alias="billToSite")
    billing_terms: Optional[BillingTermsReference] = Field(default=None, alias="billingTerms")
    bottom_comment_flag: Optional[StrictBool] = Field(default=None, alias="bottomCommentFlag")
    company: Optional[CompanyReference] = None
    company_location: Optional[SystemLocationReference] = Field(default=None, alias="companyLocation")
    config_ids: Optional[List[StrictInt]] = Field(default=None, alias="configIds")
    contact: Optional[ContactReference] = None
    currency: Optional[CurrencyReference] = None
    custom_fields: Optional[List[CustomFieldValue]] = Field(default=None, alias="customFields")
    department: Optional[SystemDepartmentReference] = None
    description: Optional[StrictStr] = None
    document_ids: Optional[List[StrictInt]] = Field(default=None, alias="documentIds")
    due_date: Optional[datetime] = Field(default=None, alias="dueDate")
    email: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    invoice_ids: Optional[List[StrictInt]] = Field(default=None, alias="invoiceIds")
    location: Optional[SystemLocationReference] = None
    notes: Optional[StrictStr] = None
    opportunity: Optional[OpportunityReference] = None
    order_date: Optional[datetime] = Field(default=None, alias="orderDate")
    phone: Optional[StrictStr] = None
    phone_ext: Optional[StrictStr] = Field(default=None, alias="phoneExt")
    po_number: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="poNumber")
    product_ids: Optional[List[StrictInt]] = Field(default=None, alias="productIds")
    restrict_downpayment_flag: Optional[StrictBool] = Field(default=None, alias="restrictDownpaymentFlag")
    sales_rep: Optional[MemberReference] = Field(default=None, alias="salesRep")
    ship_to_company: Optional[CompanyReference] = Field(default=None, alias="shipToCompany")
    ship_to_contact: Optional[ContactReference] = Field(default=None, alias="shipToContact")
    ship_to_site: Optional[SiteReference] = Field(default=None, alias="shipToSite")
    site: Optional[SiteReference] = None
    status: Optional[OrderStatusReference] = None
    sub_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="subTotal")
    tax_code: Optional[TaxCodeReference] = Field(default=None, alias="taxCode")
    tax_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="taxTotal")
    top_comment_flag: Optional[StrictBool] = Field(default=None, alias="topCommentFlag")
    total: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["_info", "billClosedFlag", "billShippedFlag", "billToCompany", "billToContact", "billToSite", "billingTerms", "bottomCommentFlag", "company", "companyLocation", "configIds", "contact", "currency", "customFields", "department", "description", "documentIds", "dueDate", "email", "id", "invoiceIds", "location", "notes", "opportunity", "orderDate", "phone", "phoneExt", "poNumber", "productIds", "restrictDownpaymentFlag", "salesRep", "shipToCompany", "shipToContact", "shipToSite", "site", "status", "subTotal", "taxCode", "taxTotal", "topCommentFlag", "total"]

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
        """Create an instance of Order from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bill_to_company
        if self.bill_to_company:
            _dict['billToCompany'] = self.bill_to_company.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bill_to_contact
        if self.bill_to_contact:
            _dict['billToContact'] = self.bill_to_contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bill_to_site
        if self.bill_to_site:
            _dict['billToSite'] = self.bill_to_site.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing_terms
        if self.billing_terms:
            _dict['billingTerms'] = self.billing_terms.to_dict()
        # override the default output from pydantic by calling `to_dict()` of company
        if self.company:
            _dict['company'] = self.company.to_dict()
        # override the default output from pydantic by calling `to_dict()` of company_location
        if self.company_location:
            _dict['companyLocation'] = self.company_location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contact
        if self.contact:
            _dict['contact'] = self.contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict['currency'] = self.currency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in custom_fields (list)
        _items = []
        if self.custom_fields:
            for _item in self.custom_fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of department
        if self.department:
            _dict['department'] = self.department.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of opportunity
        if self.opportunity:
            _dict['opportunity'] = self.opportunity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sales_rep
        if self.sales_rep:
            _dict['salesRep'] = self.sales_rep.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ship_to_company
        if self.ship_to_company:
            _dict['shipToCompany'] = self.ship_to_company.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ship_to_contact
        if self.ship_to_contact:
            _dict['shipToContact'] = self.ship_to_contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ship_to_site
        if self.ship_to_site:
            _dict['shipToSite'] = self.ship_to_site.to_dict()
        # override the default output from pydantic by calling `to_dict()` of site
        if self.site:
            _dict['site'] = self.site.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tax_code
        if self.tax_code:
            _dict['taxCode'] = self.tax_code.to_dict()
        # set to None if bill_closed_flag (nullable) is None
        # and model_fields_set contains the field
        if self.bill_closed_flag is None and "bill_closed_flag" in self.model_fields_set:
            _dict['billClosedFlag'] = None

        # set to None if bill_shipped_flag (nullable) is None
        # and model_fields_set contains the field
        if self.bill_shipped_flag is None and "bill_shipped_flag" in self.model_fields_set:
            _dict['billShippedFlag'] = None

        # set to None if bottom_comment_flag (nullable) is None
        # and model_fields_set contains the field
        if self.bottom_comment_flag is None and "bottom_comment_flag" in self.model_fields_set:
            _dict['bottomCommentFlag'] = None

        # set to None if restrict_downpayment_flag (nullable) is None
        # and model_fields_set contains the field
        if self.restrict_downpayment_flag is None and "restrict_downpayment_flag" in self.model_fields_set:
            _dict['restrictDownpaymentFlag'] = None

        # set to None if tax_total (nullable) is None
        # and model_fields_set contains the field
        if self.tax_total is None and "tax_total" in self.model_fields_set:
            _dict['taxTotal'] = None

        # set to None if top_comment_flag (nullable) is None
        # and model_fields_set contains the field
        if self.top_comment_flag is None and "top_comment_flag" in self.model_fields_set:
            _dict['topCommentFlag'] = None

        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Order from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Order) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "billClosedFlag": obj.get("billClosedFlag"),
            "billShippedFlag": obj.get("billShippedFlag"),
            "billToCompany": CompanyReference.from_dict(obj.get("billToCompany")) if obj.get("billToCompany") is not None else None,
            "billToContact": ContactReference.from_dict(obj.get("billToContact")) if obj.get("billToContact") is not None else None,
            "billToSite": SiteReference.from_dict(obj.get("billToSite")) if obj.get("billToSite") is not None else None,
            "billingTerms": BillingTermsReference.from_dict(obj.get("billingTerms")) if obj.get("billingTerms") is not None else None,
            "bottomCommentFlag": obj.get("bottomCommentFlag"),
            "company": CompanyReference.from_dict(obj.get("company")) if obj.get("company") is not None else None,
            "companyLocation": SystemLocationReference.from_dict(obj.get("companyLocation")) if obj.get("companyLocation") is not None else None,
            "configIds": obj.get("configIds"),
            "contact": ContactReference.from_dict(obj.get("contact")) if obj.get("contact") is not None else None,
            "currency": CurrencyReference.from_dict(obj.get("currency")) if obj.get("currency") is not None else None,
            "customFields": [CustomFieldValue.from_dict(_item) for _item in obj.get("customFields")] if obj.get("customFields") is not None else None,
            "department": SystemDepartmentReference.from_dict(obj.get("department")) if obj.get("department") is not None else None,
            "description": obj.get("description"),
            "documentIds": obj.get("documentIds"),
            "dueDate": obj.get("dueDate"),
            "email": obj.get("email"),
            "id": obj.get("id"),
            "invoiceIds": obj.get("invoiceIds"),
            "location": SystemLocationReference.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "notes": obj.get("notes"),
            "opportunity": OpportunityReference.from_dict(obj.get("opportunity")) if obj.get("opportunity") is not None else None,
            "orderDate": obj.get("orderDate"),
            "phone": obj.get("phone"),
            "phoneExt": obj.get("phoneExt"),
            "poNumber": obj.get("poNumber"),
            "productIds": obj.get("productIds"),
            "restrictDownpaymentFlag": obj.get("restrictDownpaymentFlag"),
            "salesRep": MemberReference.from_dict(obj.get("salesRep")) if obj.get("salesRep") is not None else None,
            "shipToCompany": CompanyReference.from_dict(obj.get("shipToCompany")) if obj.get("shipToCompany") is not None else None,
            "shipToContact": ContactReference.from_dict(obj.get("shipToContact")) if obj.get("shipToContact") is not None else None,
            "shipToSite": SiteReference.from_dict(obj.get("shipToSite")) if obj.get("shipToSite") is not None else None,
            "site": SiteReference.from_dict(obj.get("site")) if obj.get("site") is not None else None,
            "status": OrderStatusReference.from_dict(obj.get("status")) if obj.get("status") is not None else None,
            "subTotal": obj.get("subTotal"),
            "taxCode": TaxCodeReference.from_dict(obj.get("taxCode")) if obj.get("taxCode") is not None else None,
            "taxTotal": obj.get("taxTotal"),
            "topCommentFlag": obj.get("topCommentFlag"),
            "total": obj.get("total")
        })
        return _obj


