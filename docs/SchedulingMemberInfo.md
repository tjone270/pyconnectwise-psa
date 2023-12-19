# SchedulingMemberInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**last_name** | **str** |  | [optional] 
**middle_initial** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.scheduling_member_info import SchedulingMemberInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingMemberInfo from a JSON string
scheduling_member_info_instance = SchedulingMemberInfo.from_json(json)
# print the JSON string representation of the object
print SchedulingMemberInfo.to_json()

# convert the object into a dict
scheduling_member_info_dict = scheduling_member_info_instance.to_dict()
# create an instance of SchedulingMemberInfo from a dict
scheduling_member_info_form_dict = scheduling_member_info.from_dict(scheduling_member_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


