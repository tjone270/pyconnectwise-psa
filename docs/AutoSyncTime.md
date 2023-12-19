# AutoSyncTime


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**sync_time** | **str** |  | 
**time_zone** | [**TimeZoneSetupReference**](TimeZoneSetupReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.auto_sync_time import AutoSyncTime

# TODO update the JSON string below
json = "{}"
# create an instance of AutoSyncTime from a JSON string
auto_sync_time_instance = AutoSyncTime.from_json(json)
# print the JSON string representation of the object
print AutoSyncTime.to_json()

# convert the object into a dict
auto_sync_time_dict = auto_sync_time_instance.to_dict()
# create an instance of AutoSyncTime from a dict
auto_sync_time_form_dict = auto_sync_time.from_dict(auto_sync_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


