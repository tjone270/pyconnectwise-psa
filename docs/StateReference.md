# StateReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.state_reference import StateReference

# TODO update the JSON string below
json = "{}"
# create an instance of StateReference from a JSON string
state_reference_instance = StateReference.from_json(json)
# print the JSON string representation of the object
print StateReference.to_json()

# convert the object into a dict
state_reference_dict = state_reference_instance.to_dict()
# create an instance of StateReference from a dict
state_reference_form_dict = state_reference.from_dict(state_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


