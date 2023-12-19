# TrackReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.track_reference import TrackReference

# TODO update the JSON string below
json = "{}"
# create an instance of TrackReference from a JSON string
track_reference_instance = TrackReference.from_json(json)
# print the JSON string representation of the object
print TrackReference.to_json()

# convert the object into a dict
track_reference_dict = track_reference_instance.to_dict()
# create an instance of TrackReference from a dict
track_reference_form_dict = track_reference.from_dict(track_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


