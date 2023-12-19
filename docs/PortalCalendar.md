# PortalCalendar


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**adjust1_end** | **str** |  | [optional] 
**adjust1_hours** | **float** |  | [optional] 
**adjust1_start** | **str** |  | [optional] 
**adjust2_end** | **str** |  | [optional] 
**adjust2_hours** | **float** |  | [optional] 
**adjust2_start** | **str** |  | [optional] 
**adjust3_end** | **str** |  | [optional] 
**adjust3_hours** | **float** |  | [optional] 
**adjust3_start** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**week_start** | **str** |  | 

## Example

```python
from connectwise_psa.models.portal_calendar import PortalCalendar

# TODO update the JSON string below
json = "{}"
# create an instance of PortalCalendar from a JSON string
portal_calendar_instance = PortalCalendar.from_json(json)
# print the JSON string representation of the object
print PortalCalendar.to_json()

# convert the object into a dict
portal_calendar_dict = portal_calendar_instance.to_dict()
# create an instance of PortalCalendar from a dict
portal_calendar_form_dict = portal_calendar.from_dict(portal_calendar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


