# State


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**country** | [**CountryReference**](CountryReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  Max length: 50; | 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.state import State

# TODO update the JSON string below
json = "{}"
# create an instance of State from a JSON string
state_instance = State.from_json(json)
# print the JSON string representation of the object
print State.to_json()

# convert the object into a dict
state_dict = state_instance.to_dict()
# create an instance of State from a dict
state_form_dict = state.from_dict(state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


