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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from connectwise_psa.models.classification_reference import ClassificationReference
from connectwise_psa.models.company_reference import CompanyReference
from connectwise_psa.models.currency_reference import CurrencyReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GLExportExpenseBillDetail(BaseModel):
    """
    GLExportExpenseBillDetail
    """ # noqa: E501
    account_number: Optional[StrictStr] = Field(default=None, alias="accountNumber")
    billable: Optional[StrictBool] = None
    company: Optional[CompanyReference] = None
    company_advance: Optional[StrictBool] = Field(default=None, alias="companyAdvance")
    currency: Optional[CurrencyReference] = None
    document_date: Optional[StrictStr] = Field(default=None, alias="documentDate")
    expense_class: Optional[ClassificationReference] = Field(default=None, alias="expenseClass")
    gl_type_id: Optional[StrictStr] = Field(default=None, alias="glTypeId")
    id: Optional[List[StrictInt]] = None
    memo: Optional[StrictStr] = None
    reimbursable: Optional[StrictBool] = None
    total: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["accountNumber", "billable", "company", "companyAdvance", "currency", "documentDate", "expenseClass", "glTypeId", "id", "memo", "reimbursable", "total"]

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
        """Create an instance of GLExportExpenseBillDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of company
        if self.company:
            _dict['company'] = self.company.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict['currency'] = self.currency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of expense_class
        if self.expense_class:
            _dict['expenseClass'] = self.expense_class.to_dict()
        # set to None if billable (nullable) is None
        # and model_fields_set contains the field
        if self.billable is None and "billable" in self.model_fields_set:
            _dict['billable'] = None

        # set to None if company_advance (nullable) is None
        # and model_fields_set contains the field
        if self.company_advance is None and "company_advance" in self.model_fields_set:
            _dict['companyAdvance'] = None

        # set to None if reimbursable (nullable) is None
        # and model_fields_set contains the field
        if self.reimbursable is None and "reimbursable" in self.model_fields_set:
            _dict['reimbursable'] = None

        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GLExportExpenseBillDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in GLExportExpenseBillDetail) in the input: " + _key)

        _obj = cls.model_validate({
            "accountNumber": obj.get("accountNumber"),
            "billable": obj.get("billable"),
            "company": CompanyReference.from_dict(obj.get("company")) if obj.get("company") is not None else None,
            "companyAdvance": obj.get("companyAdvance"),
            "currency": CurrencyReference.from_dict(obj.get("currency")) if obj.get("currency") is not None else None,
            "documentDate": obj.get("documentDate"),
            "expenseClass": ClassificationReference.from_dict(obj.get("expenseClass")) if obj.get("expenseClass") is not None else None,
            "glTypeId": obj.get("glTypeId"),
            "id": obj.get("id"),
            "memo": obj.get("memo"),
            "reimbursable": obj.get("reimbursable"),
            "total": obj.get("total")
        })
        return _obj


