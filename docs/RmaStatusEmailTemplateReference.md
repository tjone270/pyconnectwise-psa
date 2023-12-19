# RmaStatusEmailTemplateReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.rma_status_email_template_reference import RmaStatusEmailTemplateReference

# TODO update the JSON string below
json = "{}"
# create an instance of RmaStatusEmailTemplateReference from a JSON string
rma_status_email_template_reference_instance = RmaStatusEmailTemplateReference.from_json(json)
# print the JSON string representation of the object
print RmaStatusEmailTemplateReference.to_json()

# convert the object into a dict
rma_status_email_template_reference_dict = rma_status_email_template_reference_instance.to_dict()
# create an instance of RmaStatusEmailTemplateReference from a dict
rma_status_email_template_reference_form_dict = rma_status_email_template_reference.from_dict(rma_status_email_template_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


