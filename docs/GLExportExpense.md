# GLExportExpense


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**ap_account_number** | **str** |  | [optional] 
**ap_class** | **str** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**company_account_number** | **str** |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**description** | **str** |  | [optional] 
**document_date** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**gl_class** | **str** |  | [optional] 
**gl_type_id** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**memo** | **str** |  | [optional] 
**offset** | [**GLExportExpenseOffset**](GLExportExpenseOffset.md) |  | [optional] 
**period_end_date** | **str** |  | [optional] 
**period_start_date** | **str** |  | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**total** | **float** |  | [optional] 
**vendor_number** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.gl_export_expense import GLExportExpense

# TODO update the JSON string below
json = "{}"
# create an instance of GLExportExpense from a JSON string
gl_export_expense_instance = GLExportExpense.from_json(json)
# print the JSON string representation of the object
print GLExportExpense.to_json()

# convert the object into a dict
gl_export_expense_dict = gl_export_expense_instance.to_dict()
# create an instance of GLExportExpense from a dict
gl_export_expense_form_dict = gl_export_expense.from_dict(gl_export_expense_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


