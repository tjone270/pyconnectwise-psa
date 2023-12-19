# ExpenseTaxTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.expense_tax_type_reference import ExpenseTaxTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseTaxTypeReference from a JSON string
expense_tax_type_reference_instance = ExpenseTaxTypeReference.from_json(json)
# print the JSON string representation of the object
print ExpenseTaxTypeReference.to_json()

# convert the object into a dict
expense_tax_type_reference_dict = expense_tax_type_reference_instance.to_dict()
# create an instance of ExpenseTaxTypeReference from a dict
expense_tax_type_reference_form_dict = expense_tax_type_reference.from_dict(expense_tax_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


