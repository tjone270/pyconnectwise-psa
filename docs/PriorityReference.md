# PriorityReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**level** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**sort** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.priority_reference import PriorityReference

# TODO update the JSON string below
json = "{}"
# create an instance of PriorityReference from a JSON string
priority_reference_instance = PriorityReference.from_json(json)
# print the JSON string representation of the object
print PriorityReference.to_json()

# convert the object into a dict
priority_reference_dict = priority_reference_instance.to_dict()
# create an instance of PriorityReference from a dict
priority_reference_form_dict = priority_reference.from_dict(priority_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


