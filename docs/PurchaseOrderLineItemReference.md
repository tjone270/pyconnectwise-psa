# PurchaseOrderLineItemReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.purchase_order_line_item_reference import PurchaseOrderLineItemReference

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderLineItemReference from a JSON string
purchase_order_line_item_reference_instance = PurchaseOrderLineItemReference.from_json(json)
# print the JSON string representation of the object
print PurchaseOrderLineItemReference.to_json()

# convert the object into a dict
purchase_order_line_item_reference_dict = purchase_order_line_item_reference_instance.to_dict()
# create an instance of PurchaseOrderLineItemReference from a dict
purchase_order_line_item_reference_form_dict = purchase_order_line_item_reference.from_dict(purchase_order_line_item_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


