# ServiceTemplateReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.service_template_reference import ServiceTemplateReference

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTemplateReference from a JSON string
service_template_reference_instance = ServiceTemplateReference.from_json(json)
# print the JSON string representation of the object
print ServiceTemplateReference.to_json()

# convert the object into a dict
service_template_reference_dict = service_template_reference_instance.to_dict()
# create an instance of ServiceTemplateReference from a dict
service_template_reference_form_dict = service_template_reference.from_dict(service_template_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


