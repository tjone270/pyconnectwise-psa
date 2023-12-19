# ChargeCode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**allow_all_expense_type_flag** | **bool** |  | [optional] 
**bill_time** | **str** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**expense_entry_flag** | **bool** |  | [optional] 
**expense_type_ids** | **List[int]** |  | [optional] 
**id** | **int** |  | [optional] 
**integration_xref** | **str** |  Max length: 50; | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**name** | **str** |  Max length: 50; | 
**time_entry_flag** | **bool** |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 
**work_type** | [**WorkTypeReference**](WorkTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.charge_code import ChargeCode

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeCode from a JSON string
charge_code_instance = ChargeCode.from_json(json)
# print the JSON string representation of the object
print ChargeCode.to_json()

# convert the object into a dict
charge_code_dict = charge_code_instance.to_dict()
# create an instance of ChargeCode from a dict
charge_code_form_dict = charge_code.from_dict(charge_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


