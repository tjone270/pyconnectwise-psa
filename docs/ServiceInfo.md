# ServiceInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**contact_color** | **str** |  | [optional] 
**header_color** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**member_color** | **str** |  | [optional] 
**unknown_color** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.service_info import ServiceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceInfo from a JSON string
service_info_instance = ServiceInfo.from_json(json)
# print the JSON string representation of the object
print ServiceInfo.to_json()

# convert the object into a dict
service_info_dict = service_info_instance.to_dict()
# create an instance of ServiceInfo from a dict
service_info_form_dict = service_info.from_dict(service_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


