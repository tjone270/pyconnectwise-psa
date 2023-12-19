# ChargeCodeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**allow_all_expense_type_flag** | **bool** |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**expense_entry_flag** | **bool** |  | [optional] 
**expense_type_ids** | **List[int]** |  | [optional] 
**id** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**name** | **str** |  | [optional] 
**time_entry_flag** | **bool** |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 
**work_type** | [**WorkTypeReference**](WorkTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.charge_code_info import ChargeCodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeCodeInfo from a JSON string
charge_code_info_instance = ChargeCodeInfo.from_json(json)
# print the JSON string representation of the object
print ChargeCodeInfo.to_json()

# convert the object into a dict
charge_code_info_dict = charge_code_info_instance.to_dict()
# create an instance of ChargeCodeInfo from a dict
charge_code_info_form_dict = charge_code_info.from_dict(charge_code_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


