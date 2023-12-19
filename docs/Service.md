# Service


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**allow_cc_flag** | **bool** |  | [optional] 
**allow_to_flag** | **bool** |  | [optional] 
**calendar_setup** | [**CalendarSetupReference**](CalendarSetupReference.md) |  | [optional] 
**contact_color** | **str** |  Max length: 50; | [optional] 
**contact_color_disable_flag** | **bool** |  | [optional] 
**header_color** | **str** |  Max length: 50; | [optional] 
**header_color_disable_flag** | **bool** |  | [optional] 
**hide_delimiter_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**member_color** | **str** |  Max length: 50; | [optional] 
**member_color_disable_flag** | **bool** |  | [optional] 
**schedule_span** | **str** |  | 
**sr_notify** | **str** |  | 
**unknown_color** | **str** |  Max length: 50; | [optional] 
**unknown_color_disable_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.service import Service

# TODO update the JSON string below
json = "{}"
# create an instance of Service from a JSON string
service_instance = Service.from_json(json)
# print the JSON string representation of the object
print Service.to_json()

# convert the object into a dict
service_dict = service_instance.to_dict()
# create an instance of Service from a dict
service_form_dict = service.from_dict(service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


