# OrderStatusEmailTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**body** | **str** |  | 
**copy_sender_flag** | **bool** |  | [optional] 
**email_address** | **str** |  Max length: 100; | [optional] 
**first_name** | **str** |  Max length: 100; | [optional] 
**id** | **int** |  | [optional] 
**last_name** | **str** |  Max length: 100; | [optional] 
**status** | [**OrderStatusReference**](OrderStatusReference.md) |  | [optional] 
**subject** | **str** |  Max length: 200; | 
**use_sender_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.order_status_email_template import OrderStatusEmailTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of OrderStatusEmailTemplate from a JSON string
order_status_email_template_instance = OrderStatusEmailTemplate.from_json(json)
# print the JSON string representation of the object
print OrderStatusEmailTemplate.to_json()

# convert the object into a dict
order_status_email_template_dict = order_status_email_template_instance.to_dict()
# create an instance of OrderStatusEmailTemplate from a dict
order_status_email_template_form_dict = order_status_email_template.from_dict(order_status_email_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


