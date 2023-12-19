# ServiceSubTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.service_sub_type_reference import ServiceSubTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSubTypeReference from a JSON string
service_sub_type_reference_instance = ServiceSubTypeReference.from_json(json)
# print the JSON string representation of the object
print ServiceSubTypeReference.to_json()

# convert the object into a dict
service_sub_type_reference_dict = service_sub_type_reference_instance.to_dict()
# create an instance of ServiceSubTypeReference from a dict
service_sub_type_reference_form_dict = service_sub_type_reference.from_dict(service_sub_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


