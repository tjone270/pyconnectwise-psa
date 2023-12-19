# OrderStatusEmailTemplateReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.order_status_email_template_reference import OrderStatusEmailTemplateReference

# TODO update the JSON string below
json = "{}"
# create an instance of OrderStatusEmailTemplateReference from a JSON string
order_status_email_template_reference_instance = OrderStatusEmailTemplateReference.from_json(json)
# print the JSON string representation of the object
print OrderStatusEmailTemplateReference.to_json()

# convert the object into a dict
order_status_email_template_reference_dict = order_status_email_template_reference_instance.to_dict()
# create an instance of OrderStatusEmailTemplateReference from a dict
order_status_email_template_reference_form_dict = order_status_email_template_reference.from_dict(order_status_email_template_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


