# UnpostedExpenseTaxableLevel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**tax_amount** | **float** |  | [optional] 
**tax_code_xref** | **str** |  | [optional] 
**tax_level** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.unposted_expense_taxable_level import UnpostedExpenseTaxableLevel

# TODO update the JSON string below
json = "{}"
# create an instance of UnpostedExpenseTaxableLevel from a JSON string
unposted_expense_taxable_level_instance = UnpostedExpenseTaxableLevel.from_json(json)
# print the JSON string representation of the object
print UnpostedExpenseTaxableLevel.to_json()

# convert the object into a dict
unposted_expense_taxable_level_dict = unposted_expense_taxable_level_instance.to_dict()
# create an instance of UnpostedExpenseTaxableLevel from a dict
unposted_expense_taxable_level_form_dict = unposted_expense_taxable_level.from_dict(unposted_expense_taxable_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


