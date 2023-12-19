# ExpenseEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement** | [**AgreementReference**](AgreementReference.md) |  | [optional] 
**agreement_amount** | **float** |  | [optional] 
**amount** | **float** |  | 
**bill_amount** | **float** |  | [optional] 
**billable_option** | **str** |  | [optional] 
**business_unit_id** | **int** |  | [optional] 
**charge_to_id** | **int** |  | [optional] 
**charge_to_type** | **str** | Gets or sets             company or chargeToType is required. | [optional] 
**classification** | [**ClassificationReference**](ClassificationReference.md) |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**var_date** | **datetime** |  | 
**expense_report** | [**ExpenseReportReference**](ExpenseReportReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**invoice** | [**InvoiceReference**](InvoiceReference.md) |  | [optional] 
**invoice_amount** | **float** |  | [optional] 
**location_id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**mobile_guid** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**odometer_end** | **float** |  | [optional] 
**odometer_start** | **float** |  | [optional] 
**payment_method** | [**PaymentMethodReference**](PaymentMethodReference.md) |  | [optional] 
**phase** | [**ProjectPhaseReference**](ProjectPhaseReference.md) |  | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**status** | **str** |  | [optional] 
**taxes** | [**List[ExpenseTax]**](ExpenseTax.md) |  | [optional] 
**ticket** | [**TicketReference**](TicketReference.md) |  | [optional] 
**type** | [**ExpenseTypeReference**](ExpenseTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.expense_entry import ExpenseEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseEntry from a JSON string
expense_entry_instance = ExpenseEntry.from_json(json)
# print the JSON string representation of the object
print ExpenseEntry.to_json()

# convert the object into a dict
expense_entry_dict = expense_entry_instance.to_dict()
# create an instance of ExpenseEntry from a dict
expense_entry_form_dict = expense_entry.from_dict(expense_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


