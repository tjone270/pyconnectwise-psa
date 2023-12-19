# PurchaseOrderStatusEmailTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**body** | **str** |  | [optional] 
**copy_sender_flag** | **bool** |  | [optional] 
**email_address** | **str** |  Max length: 100; | [optional] 
**first_name** | **str** |  Max length: 100; | [optional] 
**id** | **int** |  | [optional] 
**last_name** | **str** |  Max length: 100; | [optional] 
**status** | [**PurchaseOrderStatusReference**](PurchaseOrderStatusReference.md) |  | [optional] 
**subject** | **str** |  Max length: 200; | 
**use_sender_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.purchase_order_status_email_template import PurchaseOrderStatusEmailTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderStatusEmailTemplate from a JSON string
purchase_order_status_email_template_instance = PurchaseOrderStatusEmailTemplate.from_json(json)
# print the JSON string representation of the object
print PurchaseOrderStatusEmailTemplate.to_json()

# convert the object into a dict
purchase_order_status_email_template_dict = purchase_order_status_email_template_instance.to_dict()
# create an instance of PurchaseOrderStatusEmailTemplate from a dict
purchase_order_status_email_template_form_dict = purchase_order_status_email_template.from_dict(purchase_order_status_email_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


