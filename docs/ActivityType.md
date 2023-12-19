# ActivityType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**email_flag** | **bool** |  | [optional] 
**history_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**memo_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**points** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.activity_type import ActivityType

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityType from a JSON string
activity_type_instance = ActivityType.from_json(json)
# print the JSON string representation of the object
print ActivityType.to_json()

# convert the object into a dict
activity_type_dict = activity_type_instance.to_dict()
# create an instance of ActivityType from a dict
activity_type_form_dict = activity_type.from_dict(activity_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


