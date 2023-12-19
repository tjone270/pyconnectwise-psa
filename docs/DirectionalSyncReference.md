# DirectionalSyncReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.directional_sync_reference import DirectionalSyncReference

# TODO update the JSON string below
json = "{}"
# create an instance of DirectionalSyncReference from a JSON string
directional_sync_reference_instance = DirectionalSyncReference.from_json(json)
# print the JSON string representation of the object
print DirectionalSyncReference.to_json()

# convert the object into a dict
directional_sync_reference_dict = directional_sync_reference_instance.to_dict()
# create an instance of DirectionalSyncReference from a dict
directional_sync_reference_form_dict = directional_sync_reference.from_dict(directional_sync_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


