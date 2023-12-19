# GLExportExpenseBillDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**billable** | **bool** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**company_advance** | **bool** |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**document_date** | **str** |  | [optional] 
**expense_class** | [**ClassificationReference**](ClassificationReference.md) |  | [optional] 
**gl_type_id** | **str** |  | [optional] 
**id** | **List[int]** |  | [optional] 
**memo** | **str** |  | [optional] 
**reimbursable** | **bool** |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.gl_export_expense_bill_detail import GLExportExpenseBillDetail

# TODO update the JSON string below
json = "{}"
# create an instance of GLExportExpenseBillDetail from a JSON string
gl_export_expense_bill_detail_instance = GLExportExpenseBillDetail.from_json(json)
# print the JSON string representation of the object
print GLExportExpenseBillDetail.to_json()

# convert the object into a dict
gl_export_expense_bill_detail_dict = gl_export_expense_bill_detail_instance.to_dict()
# create an instance of GLExportExpenseBillDetail from a dict
gl_export_expense_bill_detail_form_dict = gl_export_expense_bill_detail.from_dict(gl_export_expense_bill_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


