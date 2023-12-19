# ExpenseTaxTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.expense_tax_type_info import ExpenseTaxTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseTaxTypeInfo from a JSON string
expense_tax_type_info_instance = ExpenseTaxTypeInfo.from_json(json)
# print the JSON string representation of the object
print ExpenseTaxTypeInfo.to_json()

# convert the object into a dict
expense_tax_type_info_dict = expense_tax_type_info_instance.to_dict()
# create an instance of ExpenseTaxTypeInfo from a dict
expense_tax_type_info_form_dict = expense_tax_type_info.from_dict(expense_tax_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


