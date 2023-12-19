# ServiceTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.service_type_reference import ServiceTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTypeReference from a JSON string
service_type_reference_instance = ServiceTypeReference.from_json(json)
# print the JSON string representation of the object
print ServiceTypeReference.to_json()

# convert the object into a dict
service_type_reference_dict = service_type_reference_instance.to_dict()
# create an instance of ServiceTypeReference from a dict
service_type_reference_form_dict = service_type_reference.from_dict(service_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


