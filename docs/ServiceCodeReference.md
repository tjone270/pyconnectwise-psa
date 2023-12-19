# ServiceCodeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.service_code_reference import ServiceCodeReference

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCodeReference from a JSON string
service_code_reference_instance = ServiceCodeReference.from_json(json)
# print the JSON string representation of the object
print ServiceCodeReference.to_json()

# convert the object into a dict
service_code_reference_dict = service_code_reference_instance.to_dict()
# create an instance of ServiceCodeReference from a dict
service_code_reference_form_dict = service_code_reference.from_dict(service_code_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


