# EmailTemplateReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.email_template_reference import EmailTemplateReference

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTemplateReference from a JSON string
email_template_reference_instance = EmailTemplateReference.from_json(json)
# print the JSON string representation of the object
print EmailTemplateReference.to_json()

# convert the object into a dict
email_template_reference_dict = email_template_reference_instance.to_dict()
# create an instance of EmailTemplateReference from a dict
email_template_reference_form_dict = email_template_reference.from_dict(email_template_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


