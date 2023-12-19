# GLExportExpenseBill


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ap_account_number** | **str** |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**detail** | [**List[GLExportExpenseBillDetail]**](GLExportExpenseBillDetail.md) |  | [optional] 
**document_date** | **str** |  | [optional] 
**document_number** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**gl_class** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**memo** | **str** |  | [optional] 
**total** | **float** |  | [optional] 
**vendor_number** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.gl_export_expense_bill import GLExportExpenseBill

# TODO update the JSON string below
json = "{}"
# create an instance of GLExportExpenseBill from a JSON string
gl_export_expense_bill_instance = GLExportExpenseBill.from_json(json)
# print the JSON string representation of the object
print GLExportExpenseBill.to_json()

# convert the object into a dict
gl_export_expense_bill_dict = gl_export_expense_bill_instance.to_dict()
# create an instance of GLExportExpenseBill from a dict
gl_export_expense_bill_form_dict = gl_export_expense_bill.from_dict(gl_export_expense_bill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


