# TimeZoneSetupInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**offset** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.time_zone_setup_info import TimeZoneSetupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TimeZoneSetupInfo from a JSON string
time_zone_setup_info_instance = TimeZoneSetupInfo.from_json(json)
# print the JSON string representation of the object
print TimeZoneSetupInfo.to_json()

# convert the object into a dict
time_zone_setup_info_dict = time_zone_setup_info_instance.to_dict()
# create an instance of TimeZoneSetupInfo from a dict
time_zone_setup_info_form_dict = time_zone_setup_info.from_dict(time_zone_setup_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


