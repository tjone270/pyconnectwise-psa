# ExpenseEntryTaxViewModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_id** | **int** |  | [optional] 
**can_delete** | **bool** |  | [optional] 
**expense_detail_rec_id** | **int** |  | [optional] 
**expense_detail_tax_rec_id** | **int** |  | [optional] 
**mobile_guid** | **str** |  | [optional] 
**tax_amount** | **float** |  | [optional] 
**tax_type** | [**GenericNameIdDTO**](GenericNameIdDTO.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.expense_entry_tax_view_model import ExpenseEntryTaxViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseEntryTaxViewModel from a JSON string
expense_entry_tax_view_model_instance = ExpenseEntryTaxViewModel.from_json(json)
# print the JSON string representation of the object
print ExpenseEntryTaxViewModel.to_json()

# convert the object into a dict
expense_entry_tax_view_model_dict = expense_entry_tax_view_model_instance.to_dict()
# create an instance of ExpenseEntryTaxViewModel from a dict
expense_entry_tax_view_model_form_dict = expense_entry_tax_view_model.from_dict(expense_entry_tax_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


