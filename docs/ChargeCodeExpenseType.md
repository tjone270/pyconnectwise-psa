# ChargeCodeExpenseType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**charge_code** | [**ChargeCodeReference**](ChargeCodeReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**type** | [**ExpenseTypeReference**](ExpenseTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.charge_code_expense_type import ChargeCodeExpenseType

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeCodeExpenseType from a JSON string
charge_code_expense_type_instance = ChargeCodeExpenseType.from_json(json)
# print the JSON string representation of the object
print ChargeCodeExpenseType.to_json()

# convert the object into a dict
charge_code_expense_type_dict = charge_code_expense_type_instance.to_dict()
# create an instance of ChargeCodeExpenseType from a dict
charge_code_expense_type_form_dict = charge_code_expense_type.from_dict(charge_code_expense_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


