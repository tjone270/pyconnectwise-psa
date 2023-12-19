# PriorityInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.priority_info import PriorityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PriorityInfo from a JSON string
priority_info_instance = PriorityInfo.from_json(json)
# print the JSON string representation of the object
print PriorityInfo.to_json()

# convert the object into a dict
priority_info_dict = priority_info_instance.to_dict()
# create an instance of PriorityInfo from a dict
priority_info_form_dict = priority_info.from_dict(priority_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


