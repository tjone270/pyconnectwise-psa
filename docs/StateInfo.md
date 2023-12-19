# StateInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**country** | [**CountryReference**](CountryReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.state_info import StateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StateInfo from a JSON string
state_info_instance = StateInfo.from_json(json)
# print the JSON string representation of the object
print StateInfo.to_json()

# convert the object into a dict
state_info_dict = state_info_instance.to_dict()
# create an instance of StateInfo from a dict
state_info_form_dict = state_info.from_dict(state_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


