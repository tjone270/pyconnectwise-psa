# ServiceStatusReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**sort** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.service_status_reference import ServiceStatusReference

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStatusReference from a JSON string
service_status_reference_instance = ServiceStatusReference.from_json(json)
# print the JSON string representation of the object
print ServiceStatusReference.to_json()

# convert the object into a dict
service_status_reference_dict = service_status_reference_instance.to_dict()
# create an instance of ServiceStatusReference from a dict
service_status_reference_form_dict = service_status_reference.from_dict(service_status_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


