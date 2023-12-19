# ServiceSourceReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.service_source_reference import ServiceSourceReference

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSourceReference from a JSON string
service_source_reference_instance = ServiceSourceReference.from_json(json)
# print the JSON string representation of the object
print ServiceSourceReference.to_json()

# convert the object into a dict
service_source_reference_dict = service_source_reference_instance.to_dict()
# create an instance of ServiceSourceReference from a dict
service_source_reference_form_dict = service_source_reference.from_dict(service_source_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


