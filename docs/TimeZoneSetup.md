# TimeZoneSetup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**daylight_savings_flag** | **bool** | Determined based on system library value for specified timeZone.             Not able to be used in query params at this time | [optional] 
**default_flag** | **bool** | Identifies the default system time zone setup | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**offset** | **float** | The hours offset from UTC (+/-) | [optional] 
**time_zone** | [**TimeZoneReference**](TimeZoneReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.time_zone_setup import TimeZoneSetup

# TODO update the JSON string below
json = "{}"
# create an instance of TimeZoneSetup from a JSON string
time_zone_setup_instance = TimeZoneSetup.from_json(json)
# print the JSON string representation of the object
print TimeZoneSetup.to_json()

# convert the object into a dict
time_zone_setup_dict = time_zone_setup_instance.to_dict()
# create an instance of TimeZoneSetup from a dict
time_zone_setup_form_dict = time_zone_setup.from_dict(time_zone_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


