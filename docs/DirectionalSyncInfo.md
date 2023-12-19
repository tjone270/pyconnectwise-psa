# DirectionalSyncInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.directional_sync_info import DirectionalSyncInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DirectionalSyncInfo from a JSON string
directional_sync_info_instance = DirectionalSyncInfo.from_json(json)
# print the JSON string representation of the object
print DirectionalSyncInfo.to_json()

# convert the object into a dict
directional_sync_info_dict = directional_sync_info_instance.to_dict()
# create an instance of DirectionalSyncInfo from a dict
directional_sync_info_form_dict = directional_sync_info.from_dict(directional_sync_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


