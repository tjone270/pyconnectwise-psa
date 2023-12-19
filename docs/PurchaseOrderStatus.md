# PurchaseOrderStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**closed_flag** | **bool** |  | [optional] 
**default_closed_flag** | **bool** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**email_template** | [**PurchaseOrderStatusEmailTemplateReference**](PurchaseOrderStatusEmailTemplateReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**sort_order** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.purchase_order_status import PurchaseOrderStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderStatus from a JSON string
purchase_order_status_instance = PurchaseOrderStatus.from_json(json)
# print the JSON string representation of the object
print PurchaseOrderStatus.to_json()

# convert the object into a dict
purchase_order_status_dict = purchase_order_status_instance.to_dict()
# create an instance of PurchaseOrderStatus from a dict
purchase_order_status_form_dict = purchase_order_status.from_dict(purchase_order_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


