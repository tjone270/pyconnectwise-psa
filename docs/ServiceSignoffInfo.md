# ServiceSignoffInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.service_signoff_info import ServiceSignoffInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSignoffInfo from a JSON string
service_signoff_info_instance = ServiceSignoffInfo.from_json(json)
# print the JSON string representation of the object
print ServiceSignoffInfo.to_json()

# convert the object into a dict
service_signoff_info_dict = service_signoff_info_instance.to_dict()
# create an instance of ServiceSignoffInfo from a dict
service_signoff_info_form_dict = service_signoff_info.from_dict(service_signoff_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


