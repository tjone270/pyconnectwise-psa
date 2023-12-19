# WorkRole


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**add_all_agreement_exclusions** | **bool** | Used only on create to add the work role to all agreement and agreement type exclusion lists | [optional] 
**add_all_locations** | **bool** |  | [optional] 
**hourly_rate** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**integration_xref** | **str** |  Max length: 50; | [optional] 
**location_ids** | **List[int]** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**remove_all_locations** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.work_role import WorkRole

# TODO update the JSON string below
json = "{}"
# create an instance of WorkRole from a JSON string
work_role_instance = WorkRole.from_json(json)
# print the JSON string representation of the object
print WorkRole.to_json()

# convert the object into a dict
work_role_dict = work_role_instance.to_dict()
# create an instance of WorkRole from a dict
work_role_form_dict = work_role.from_dict(work_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


