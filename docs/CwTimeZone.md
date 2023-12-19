# CwTimeZone


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**daylight_savings_flag** | **bool** | Determined based on system library value for specified timeZone.             Not able to be used in query params at this time. | [optional] 
**end_date** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**offset** | **float** | The hours offset (+/-). | [optional] 
**start_date** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.cw_time_zone import CwTimeZone

# TODO update the JSON string below
json = "{}"
# create an instance of CwTimeZone from a JSON string
cw_time_zone_instance = CwTimeZone.from_json(json)
# print the JSON string representation of the object
print CwTimeZone.to_json()

# convert the object into a dict
cw_time_zone_dict = cw_time_zone_instance.to_dict()
# create an instance of CwTimeZone from a dict
cw_time_zone_form_dict = cw_time_zone.from_dict(cw_time_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


