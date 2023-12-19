# ServiceSignoffReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.service_signoff_reference import ServiceSignoffReference

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSignoffReference from a JSON string
service_signoff_reference_instance = ServiceSignoffReference.from_json(json)
# print the JSON string representation of the object
print ServiceSignoffReference.to_json()

# convert the object into a dict
service_signoff_reference_dict = service_signoff_reference_instance.to_dict()
# create an instance of ServiceSignoffReference from a dict
service_signoff_reference_form_dict = service_signoff_reference.from_dict(service_signoff_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


