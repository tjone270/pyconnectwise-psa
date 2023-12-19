# Track


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 100; | 
**notify_action_ids** | **List[int]** |  | [optional] 

## Example

```python
from connectwise_psa.models.track import Track

# TODO update the JSON string below
json = "{}"
# create an instance of Track from a JSON string
track_instance = Track.from_json(json)
# print the JSON string representation of the object
print Track.to_json()

# convert the object into a dict
track_dict = track_instance.to_dict()
# create an instance of Track from a dict
track_form_dict = track.from_dict(track_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


