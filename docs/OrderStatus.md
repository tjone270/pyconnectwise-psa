# OrderStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**closed_flag** | **bool** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**email_template** | [**OrderStatusEmailTemplateReference**](OrderStatusEmailTemplateReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**sort_order** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.order_status import OrderStatus

# TODO update the JSON string below
json = "{}"
# create an instance of OrderStatus from a JSON string
order_status_instance = OrderStatus.from_json(json)
# print the JSON string representation of the object
print OrderStatus.to_json()

# convert the object into a dict
order_status_dict = order_status_instance.to_dict()
# create an instance of OrderStatus from a dict
order_status_form_dict = order_status.from_dict(order_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


