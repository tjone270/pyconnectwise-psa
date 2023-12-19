# ExpenseType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**advanced_amount_flag** | **bool** |  | [optional] 
**amount_caption** | **str** |  | 
**bill_expenses** | **str** |  | 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**integration_x_ref** | **str** |  Max length: 50; | [optional] 
**invoice_markup_amount** | **float** |  | [optional] 
**invoice_markup_option** | **str** |  | 
**max_amount** | **float** |  | [optional] 
**mileage_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 30; | 
**quantity_flag** | **bool** |  | [optional] 
**reimbursement_rate** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.expense_type import ExpenseType

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseType from a JSON string
expense_type_instance = ExpenseType.from_json(json)
# print the JSON string representation of the object
print ExpenseType.to_json()

# convert the object into a dict
expense_type_dict = expense_type_instance.to_dict()
# create an instance of ExpenseType from a dict
expense_type_form_dict = expense_type.from_dict(expense_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


