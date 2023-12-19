# PurchaseOrderStatusEmailTemplateReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.purchase_order_status_email_template_reference import PurchaseOrderStatusEmailTemplateReference

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderStatusEmailTemplateReference from a JSON string
purchase_order_status_email_template_reference_instance = PurchaseOrderStatusEmailTemplateReference.from_json(json)
# print the JSON string representation of the object
print PurchaseOrderStatusEmailTemplateReference.to_json()

# convert the object into a dict
purchase_order_status_email_template_reference_dict = purchase_order_status_email_template_reference_instance.to_dict()
# create an instance of PurchaseOrderStatusEmailTemplateReference from a dict
purchase_order_status_email_template_reference_form_dict = purchase_order_status_email_template_reference.from_dict(purchase_order_status_email_template_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


