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
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from connectwise_psa.models.agreement_reference import AgreementReference
from connectwise_psa.models.charge_code_reference import ChargeCodeReference
from connectwise_psa.models.company_reference import CompanyReference
from connectwise_psa.models.currency_reference import CurrencyReference
from connectwise_psa.models.expense_type_reference import ExpenseTypeReference
from connectwise_psa.models.member_reference import MemberReference
from connectwise_psa.models.payment_method_reference import PaymentMethodReference
from connectwise_psa.models.project_phase_reference import ProjectPhaseReference
from connectwise_psa.models.project_reference import ProjectReference
from connectwise_psa.models.tax_code_reference import TaxCodeReference
from connectwise_psa.models.ticket_reference import TicketReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UnpostedExpense(BaseModel):
    """
    UnpostedExpense
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    account_number: Optional[StrictStr] = Field(default=None, alias="accountNumber")
    agreement: Optional[AgreementReference] = None
    agreement_amount_covered: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="agreementAmountCovered")
    avalara_tax_flag: Optional[StrictBool] = Field(default=None, description="Used to determine if Avalara tax is enabled.", alias="avalaraTaxFlag")
    billable_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="billableAmount")
    charge_code: Optional[ChargeCodeReference] = Field(default=None, alias="chargeCode")
    charge_description: Optional[StrictStr] = Field(default=None, alias="chargeDescription")
    city_tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="cityTaxAmount")
    city_tax_flag: Optional[StrictBool] = Field(default=None, description="Set to true if transaction is taxable at the city level.", alias="cityTaxFlag")
    city_tax_xref: Optional[StrictStr] = Field(default=None, alias="cityTaxXref")
    classification: Optional[StrictStr] = None
    company: Optional[CompanyReference] = None
    composite_tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="compositeTaxAmount")
    composite_tax_flag: Optional[StrictBool] = Field(default=None, description="Set to true if transaction is taxable at the composite level.", alias="compositeTaxFlag")
    composite_tax_xref: Optional[StrictStr] = Field(default=None, alias="compositeTaxXref")
    country_tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="countryTaxAmount")
    country_tax_flag: Optional[StrictBool] = Field(default=None, description="Set to true if transaction is taxable at the country level.", alias="countryTaxFlag")
    country_tax_xref: Optional[StrictStr] = Field(default=None, alias="countryTaxXref")
    county_tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="countyTaxAmount")
    county_tax_flag: Optional[StrictBool] = Field(default=None, description="Set to true if transaction is taxable at the county level.", alias="countyTaxFlag")
    county_tax_xref: Optional[StrictStr] = Field(default=None, alias="countyTaxXref")
    credit_account: Optional[StrictStr] = Field(default=None, alias="creditAccount")
    currency: Optional[CurrencyReference] = None
    date_closed: Optional[StrictStr] = Field(default=None, alias="dateClosed")
    date_expense: Optional[StrictStr] = Field(default=None, alias="dateExpense")
    department_id: Optional[StrictInt] = Field(default=None, alias="departmentId")
    expense_detail_id: Optional[StrictInt] = Field(default=None, alias="expenseDetailId")
    expense_type: Optional[ExpenseTypeReference] = Field(default=None, alias="expenseType")
    gl_type: Optional[StrictStr] = Field(default=None, alias="glType")
    id: Optional[StrictInt] = None
    in_policy: Optional[StrictBool] = Field(default=None, alias="inPolicy")
    item_taxable_flag: Optional[StrictBool] = Field(default=None, alias="itemTaxableFlag")
    level_six_tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="levelSixTaxAmount")
    level_six_tax_flag: Optional[StrictBool] = Field(default=None, description="Set to true if transaction is taxable at level six.", alias="levelSixTaxFlag")
    level_six_tax_xref: Optional[StrictStr] = Field(default=None, alias="levelSixTaxXref")
    location_id: Optional[StrictInt] = Field(default=None, alias="locationId")
    member: Optional[MemberReference] = None
    non_billable_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="nonBillableAmount")
    payment_method: Optional[PaymentMethodReference] = Field(default=None, alias="paymentMethod")
    project: Optional[ProjectReference] = None
    project_phase: Optional[ProjectPhaseReference] = Field(default=None, alias="projectPhase")
    sales_tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="salesTaxAmount")
    state_tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="stateTaxAmount")
    state_tax_flag: Optional[StrictBool] = Field(default=None, description="Set to true if transaction is taxable at the state level.", alias="stateTaxFlag")
    state_tax_xref: Optional[StrictStr] = Field(default=None, alias="stateTaxXref")
    tax_code: Optional[TaxCodeReference] = Field(default=None, alias="taxCode")
    ticket: Optional[TicketReference] = None
    total: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["_info", "accountNumber", "agreement", "agreementAmountCovered", "avalaraTaxFlag", "billableAmount", "chargeCode", "chargeDescription", "cityTaxAmount", "cityTaxFlag", "cityTaxXref", "classification", "company", "compositeTaxAmount", "compositeTaxFlag", "compositeTaxXref", "countryTaxAmount", "countryTaxFlag", "countryTaxXref", "countyTaxAmount", "countyTaxFlag", "countyTaxXref", "creditAccount", "currency", "dateClosed", "dateExpense", "departmentId", "expenseDetailId", "expenseType", "glType", "id", "inPolicy", "itemTaxableFlag", "levelSixTaxAmount", "levelSixTaxFlag", "levelSixTaxXref", "locationId", "member", "nonBillableAmount", "paymentMethod", "project", "projectPhase", "salesTaxAmount", "stateTaxAmount", "stateTaxFlag", "stateTaxXref", "taxCode", "ticket", "total"]

    @field_validator('classification')
    def classification_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NonReimbursable', 'Reimbursable', 'Personal'):
            raise ValueError("must be one of enum values ('NonReimbursable', 'Reimbursable', 'Personal')")
        return value

    @field_validator('gl_type')
    def gl_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('AP', 'AR', 'EE', 'EI', 'EO', 'IA', 'IT', 'P', 'PF', 'R', 'RA', 'RD', 'RE', 'RP', 'ST', 'SD', 'ET', 'FT', 'PT', 'WP', 'WR'):
            raise ValueError("must be one of enum values ('AP', 'AR', 'EE', 'EI', 'EO', 'IA', 'IT', 'P', 'PF', 'R', 'RA', 'RD', 'RE', 'RP', 'ST', 'SD', 'ET', 'FT', 'PT', 'WP', 'WR')")
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
        """Create an instance of UnpostedExpense from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of charge_code
        if self.charge_code:
            _dict['chargeCode'] = self.charge_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of company
        if self.company:
            _dict['company'] = self.company.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict['currency'] = self.currency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of expense_type
        if self.expense_type:
            _dict['expenseType'] = self.expense_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of member
        if self.member:
            _dict['member'] = self.member.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_method
        if self.payment_method:
            _dict['paymentMethod'] = self.payment_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project_phase
        if self.project_phase:
            _dict['projectPhase'] = self.project_phase.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tax_code
        if self.tax_code:
            _dict['taxCode'] = self.tax_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ticket
        if self.ticket:
            _dict['ticket'] = self.ticket.to_dict()
        # set to None if agreement_amount_covered (nullable) is None
        # and model_fields_set contains the field
        if self.agreement_amount_covered is None and "agreement_amount_covered" in self.model_fields_set:
            _dict['agreementAmountCovered'] = None

        # set to None if avalara_tax_flag (nullable) is None
        # and model_fields_set contains the field
        if self.avalara_tax_flag is None and "avalara_tax_flag" in self.model_fields_set:
            _dict['avalaraTaxFlag'] = None

        # set to None if billable_amount (nullable) is None
        # and model_fields_set contains the field
        if self.billable_amount is None and "billable_amount" in self.model_fields_set:
            _dict['billableAmount'] = None

        # set to None if city_tax_amount (nullable) is None
        # and model_fields_set contains the field
        if self.city_tax_amount is None and "city_tax_amount" in self.model_fields_set:
            _dict['cityTaxAmount'] = None

        # set to None if city_tax_flag (nullable) is None
        # and model_fields_set contains the field
        if self.city_tax_flag is None and "city_tax_flag" in self.model_fields_set:
            _dict['cityTaxFlag'] = None

        # set to None if classification (nullable) is None
        # and model_fields_set contains the field
        if self.classification is None and "classification" in self.model_fields_set:
            _dict['classification'] = None

        # set to None if composite_tax_amount (nullable) is None
        # and model_fields_set contains the field
        if self.composite_tax_amount is None and "composite_tax_amount" in self.model_fields_set:
            _dict['compositeTaxAmount'] = None

        # set to None if composite_tax_flag (nullable) is None
        # and model_fields_set contains the field
        if self.composite_tax_flag is None and "composite_tax_flag" in self.model_fields_set:
            _dict['compositeTaxFlag'] = None

        # set to None if country_tax_amount (nullable) is None
        # and model_fields_set contains the field
        if self.country_tax_amount is None and "country_tax_amount" in self.model_fields_set:
            _dict['countryTaxAmount'] = None

        # set to None if country_tax_flag (nullable) is None
        # and model_fields_set contains the field
        if self.country_tax_flag is None and "country_tax_flag" in self.model_fields_set:
            _dict['countryTaxFlag'] = None

        # set to None if county_tax_amount (nullable) is None
        # and model_fields_set contains the field
        if self.county_tax_amount is None and "county_tax_amount" in self.model_fields_set:
            _dict['countyTaxAmount'] = None

        # set to None if county_tax_flag (nullable) is None
        # and model_fields_set contains the field
        if self.county_tax_flag is None and "county_tax_flag" in self.model_fields_set:
            _dict['countyTaxFlag'] = None

        # set to None if department_id (nullable) is None
        # and model_fields_set contains the field
        if self.department_id is None and "department_id" in self.model_fields_set:
            _dict['departmentId'] = None

        # set to None if expense_detail_id (nullable) is None
        # and model_fields_set contains the field
        if self.expense_detail_id is None and "expense_detail_id" in self.model_fields_set:
            _dict['expenseDetailId'] = None

        # set to None if gl_type (nullable) is None
        # and model_fields_set contains the field
        if self.gl_type is None and "gl_type" in self.model_fields_set:
            _dict['glType'] = None

        # set to None if in_policy (nullable) is None
        # and model_fields_set contains the field
        if self.in_policy is None and "in_policy" in self.model_fields_set:
            _dict['inPolicy'] = None

        # set to None if item_taxable_flag (nullable) is None
        # and model_fields_set contains the field
        if self.item_taxable_flag is None and "item_taxable_flag" in self.model_fields_set:
            _dict['itemTaxableFlag'] = None

        # set to None if level_six_tax_amount (nullable) is None
        # and model_fields_set contains the field
        if self.level_six_tax_amount is None and "level_six_tax_amount" in self.model_fields_set:
            _dict['levelSixTaxAmount'] = None

        # set to None if level_six_tax_flag (nullable) is None
        # and model_fields_set contains the field
        if self.level_six_tax_flag is None and "level_six_tax_flag" in self.model_fields_set:
            _dict['levelSixTaxFlag'] = None

        # set to None if location_id (nullable) is None
        # and model_fields_set contains the field
        if self.location_id is None and "location_id" in self.model_fields_set:
            _dict['locationId'] = None

        # set to None if non_billable_amount (nullable) is None
        # and model_fields_set contains the field
        if self.non_billable_amount is None and "non_billable_amount" in self.model_fields_set:
            _dict['nonBillableAmount'] = None

        # set to None if sales_tax_amount (nullable) is None
        # and model_fields_set contains the field
        if self.sales_tax_amount is None and "sales_tax_amount" in self.model_fields_set:
            _dict['salesTaxAmount'] = None

        # set to None if state_tax_amount (nullable) is None
        # and model_fields_set contains the field
        if self.state_tax_amount is None and "state_tax_amount" in self.model_fields_set:
            _dict['stateTaxAmount'] = None

        # set to None if state_tax_flag (nullable) is None
        # and model_fields_set contains the field
        if self.state_tax_flag is None and "state_tax_flag" in self.model_fields_set:
            _dict['stateTaxFlag'] = None

        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UnpostedExpense from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in UnpostedExpense) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "accountNumber": obj.get("accountNumber"),
            "agreement": AgreementReference.from_dict(obj.get("agreement")) if obj.get("agreement") is not None else None,
            "agreementAmountCovered": obj.get("agreementAmountCovered"),
            "avalaraTaxFlag": obj.get("avalaraTaxFlag"),
            "billableAmount": obj.get("billableAmount"),
            "chargeCode": ChargeCodeReference.from_dict(obj.get("chargeCode")) if obj.get("chargeCode") is not None else None,
            "chargeDescription": obj.get("chargeDescription"),
            "cityTaxAmount": obj.get("cityTaxAmount"),
            "cityTaxFlag": obj.get("cityTaxFlag"),
            "cityTaxXref": obj.get("cityTaxXref"),
            "classification": obj.get("classification"),
            "company": CompanyReference.from_dict(obj.get("company")) if obj.get("company") is not None else None,
            "compositeTaxAmount": obj.get("compositeTaxAmount"),
            "compositeTaxFlag": obj.get("compositeTaxFlag"),
            "compositeTaxXref": obj.get("compositeTaxXref"),
            "countryTaxAmount": obj.get("countryTaxAmount"),
            "countryTaxFlag": obj.get("countryTaxFlag"),
            "countryTaxXref": obj.get("countryTaxXref"),
            "countyTaxAmount": obj.get("countyTaxAmount"),
            "countyTaxFlag": obj.get("countyTaxFlag"),
            "countyTaxXref": obj.get("countyTaxXref"),
            "creditAccount": obj.get("creditAccount"),
            "currency": CurrencyReference.from_dict(obj.get("currency")) if obj.get("currency") is not None else None,
            "dateClosed": obj.get("dateClosed"),
            "dateExpense": obj.get("dateExpense"),
            "departmentId": obj.get("departmentId"),
            "expenseDetailId": obj.get("expenseDetailId"),
            "expenseType": ExpenseTypeReference.from_dict(obj.get("expenseType")) if obj.get("expenseType") is not None else None,
            "glType": obj.get("glType"),
            "id": obj.get("id"),
            "inPolicy": obj.get("inPolicy"),
            "itemTaxableFlag": obj.get("itemTaxableFlag"),
            "levelSixTaxAmount": obj.get("levelSixTaxAmount"),
            "levelSixTaxFlag": obj.get("levelSixTaxFlag"),
            "levelSixTaxXref": obj.get("levelSixTaxXref"),
            "locationId": obj.get("locationId"),
            "member": MemberReference.from_dict(obj.get("member")) if obj.get("member") is not None else None,
            "nonBillableAmount": obj.get("nonBillableAmount"),
            "paymentMethod": PaymentMethodReference.from_dict(obj.get("paymentMethod")) if obj.get("paymentMethod") is not None else None,
            "project": ProjectReference.from_dict(obj.get("project")) if obj.get("project") is not None else None,
            "projectPhase": ProjectPhaseReference.from_dict(obj.get("projectPhase")) if obj.get("projectPhase") is not None else None,
            "salesTaxAmount": obj.get("salesTaxAmount"),
            "stateTaxAmount": obj.get("stateTaxAmount"),
            "stateTaxFlag": obj.get("stateTaxFlag"),
            "stateTaxXref": obj.get("stateTaxXref"),
            "taxCode": TaxCodeReference.from_dict(obj.get("taxCode")) if obj.get("taxCode") is not None else None,
            "ticket": TicketReference.from_dict(obj.get("ticket")) if obj.get("ticket") is not None else None,
            "total": obj.get("total")
        })
        return _obj

