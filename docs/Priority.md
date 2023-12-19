# Priority


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**color** | **str** |  | 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**image_link** | **str** |  | [optional] 
**level** | **str** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**sort_order** | **int** |  | [optional] 
**urgency_sort_order** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.priority import Priority

# TODO update the JSON string below
json = "{}"
# create an instance of Priority from a JSON string
priority_instance = Priority.from_json(json)
# print the JSON string representation of the object
print Priority.to_json()

# convert the object into a dict
priority_dict = priority_instance.to_dict()
# create an instance of Priority from a dict
priority_form_dict = priority.from_dict(priority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


