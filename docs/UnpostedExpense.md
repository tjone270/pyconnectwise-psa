# UnpostedExpense


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**account_number** | **str** |  | [optional] 
**agreement** | [**AgreementReference**](AgreementReference.md) |  | [optional] 
**agreement_amount_covered** | **float** |  | [optional] 
**avalara_tax_flag** | **bool** | Used to determine if Avalara tax is enabled. | [optional] 
**billable_amount** | **float** |  | [optional] 
**charge_code** | [**ChargeCodeReference**](ChargeCodeReference.md) |  | [optional] 
**charge_description** | **str** |  | [optional] 
**city_tax_amount** | **float** |  | [optional] 
**city_tax_flag** | **bool** | Set to true if transaction is taxable at the city level. | [optional] 
**city_tax_xref** | **str** |  | [optional] 
**classification** | **str** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**composite_tax_amount** | **float** |  | [optional] 
**composite_tax_flag** | **bool** | Set to true if transaction is taxable at the composite level. | [optional] 
**composite_tax_xref** | **str** |  | [optional] 
**country_tax_amount** | **float** |  | [optional] 
**country_tax_flag** | **bool** | Set to true if transaction is taxable at the country level. | [optional] 
**country_tax_xref** | **str** |  | [optional] 
**county_tax_amount** | **float** |  | [optional] 
**county_tax_flag** | **bool** | Set to true if transaction is taxable at the county level. | [optional] 
**county_tax_xref** | **str** |  | [optional] 
**credit_account** | **str** |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**date_closed** | **str** |  | [optional] 
**date_expense** | **str** |  | [optional] 
**department_id** | **int** |  | [optional] 
**expense_detail_id** | **int** |  | [optional] 
**expense_type** | [**ExpenseTypeReference**](ExpenseTypeReference.md) |  | [optional] 
**gl_type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**in_policy** | **bool** |  | [optional] 
**item_taxable_flag** | **bool** |  | [optional] 
**level_six_tax_amount** | **float** |  | [optional] 
**level_six_tax_flag** | **bool** | Set to true if transaction is taxable at level six. | [optional] 
**level_six_tax_xref** | **str** |  | [optional] 
**location_id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**non_billable_amount** | **float** |  | [optional] 
**payment_method** | [**PaymentMethodReference**](PaymentMethodReference.md) |  | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**project_phase** | [**ProjectPhaseReference**](ProjectPhaseReference.md) |  | [optional] 
**sales_tax_amount** | **float** |  | [optional] 
**state_tax_amount** | **float** |  | [optional] 
**state_tax_flag** | **bool** | Set to true if transaction is taxable at the state level. | [optional] 
**state_tax_xref** | **str** |  | [optional] 
**tax_code** | [**TaxCodeReference**](TaxCodeReference.md) |  | [optional] 
**ticket** | [**TicketReference**](TicketReference.md) |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.unposted_expense import UnpostedExpense

# TODO update the JSON string below
json = "{}"
# create an instance of UnpostedExpense from a JSON string
unposted_expense_instance = UnpostedExpense.from_json(json)
# print the JSON string representation of the object
print UnpostedExpense.to_json()

# convert the object into a dict
unposted_expense_dict = unposted_expense_instance.to_dict()
# create an instance of UnpostedExpense from a dict
unposted_expense_form_dict = unposted_expense.from_dict(unposted_expense_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


