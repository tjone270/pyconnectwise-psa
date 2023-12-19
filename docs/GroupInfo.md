# GroupInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.group_info import GroupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GroupInfo from a JSON string
group_info_instance = GroupInfo.from_json(json)
# print the JSON string representation of the object
print GroupInfo.to_json()

# convert the object into a dict
group_info_dict = group_info_instance.to_dict()
# create an instance of GroupInfo from a dict
group_info_form_dict = group_info.from_dict(group_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


