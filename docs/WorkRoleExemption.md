# WorkRoleExemption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**taxable_levels** | **List[int]** |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | 

## Example

```python
from connectwise_psa.models.work_role_exemption import WorkRoleExemption

# TODO update the JSON string below
json = "{}"
# create an instance of WorkRoleExemption from a JSON string
work_role_exemption_instance = WorkRoleExemption.from_json(json)
# print the JSON string representation of the object
print WorkRoleExemption.to_json()

# convert the object into a dict
work_role_exemption_dict = work_role_exemption_instance.to_dict()
# create an instance of WorkRoleExemption from a dict
work_role_exemption_form_dict = work_role_exemption.from_dict(work_role_exemption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


