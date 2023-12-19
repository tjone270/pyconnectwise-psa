# ServiceEmailTemplateReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.service_email_template_reference import ServiceEmailTemplateReference

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceEmailTemplateReference from a JSON string
service_email_template_reference_instance = ServiceEmailTemplateReference.from_json(json)
# print the JSON string representation of the object
print ServiceEmailTemplateReference.to_json()

# convert the object into a dict
service_email_template_reference_dict = service_email_template_reference_instance.to_dict()
# create an instance of ServiceEmailTemplateReference from a dict
service_email_template_reference_form_dict = service_email_template_reference.from_dict(service_email_template_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


