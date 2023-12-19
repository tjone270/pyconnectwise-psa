# ServiceLocation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 30; | 
**where** | **str** |  | 

## Example

```python
from connectwise_psa.models.service_location import ServiceLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLocation from a JSON string
service_location_instance = ServiceLocation.from_json(json)
# print the JSON string representation of the object
print ServiceLocation.to_json()

# convert the object into a dict
service_location_dict = service_location_instance.to_dict()
# create an instance of ServiceLocation from a dict
service_location_form_dict = service_location.from_dict(service_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


