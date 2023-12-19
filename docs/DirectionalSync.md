# DirectionalSync


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.directional_sync import DirectionalSync

# TODO update the JSON string below
json = "{}"
# create an instance of DirectionalSync from a JSON string
directional_sync_instance = DirectionalSync.from_json(json)
# print the JSON string representation of the object
print DirectionalSync.to_json()

# convert the object into a dict
directional_sync_dict = directional_sync_instance.to_dict()
# create an instance of DirectionalSync from a dict
directional_sync_form_dict = directional_sync.from_dict(directional_sync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


