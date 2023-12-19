# ExpenseTax


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**type** | [**ExpenseTaxTypeReference**](ExpenseTaxTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.expense_tax import ExpenseTax

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseTax from a JSON string
expense_tax_instance = ExpenseTax.from_json(json)
# print the JSON string representation of the object
print ExpenseTax.to_json()

# convert the object into a dict
expense_tax_dict = expense_tax_instance.to_dict()
# create an instance of ExpenseTax from a dict
expense_tax_form_dict = expense_tax.from_dict(expense_tax_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


