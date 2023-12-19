# PurchaseOrderLineItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**backordered_flag** | **bool** |  | [optional] 
**canceled_by** | **str** |  | [optional] 
**canceled_flag** | **bool** |  | [optional] 
**canceled_reason** | **str** |  Max length: 100; | [optional] 
**closed_flag** | **bool** |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**date_canceled** | **datetime** |  | [optional] 
**date_canceled_utc** | **datetime** |  | [optional] 
**date_received** | **datetime** |  | [optional] 
**description** | **str** |  Max length: 6000; | 
**display_internal_notes_flag** | **bool** |  | [optional] 
**expected_ship_date** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**internal_notes** | **str** |  Max length: 1000; | [optional] 
**line_number** | **int** |  | 
**packing_slip** | **str** |  Max length: 50; | [optional] 
**product** | [**IvItemReference**](IvItemReference.md) |  | [optional] 
**purchase_order_id** | **int** |  | [optional] 
**quantity** | **float** |  | 
**received_quantity** | **int** |  | [optional] 
**received_status** | **str** |  | [optional] 
**serial_numbers** | **str** |  | [optional] 
**ship_date** | **datetime** |  | [optional] 
**ship_set** | **str** |  Max length: 10; | [optional] 
**shipment_method** | [**ShipmentMethodReference**](ShipmentMethodReference.md) |  | [optional] 
**tax** | **float** |  | [optional] 
**tracking_number** | **str** |  Max length: 50; | [optional] 
**unit_cost** | **float** |  | [optional] 
**unit_of_measure** | [**UnitOfMeasureReference**](UnitOfMeasureReference.md) |  | [optional] 
**vendor_order_number** | **str** |  Max length: 50; | [optional] 
**vendor_sku** | **str** |  Max length: 50; | [optional] 
**warehouse** | [**WarehouseReference**](WarehouseReference.md) |  | [optional] 
**warehouse_bin** | [**WarehouseBinReference**](WarehouseBinReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.purchase_order_line_item import PurchaseOrderLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderLineItem from a JSON string
purchase_order_line_item_instance = PurchaseOrderLineItem.from_json(json)
# print the JSON string representation of the object
print PurchaseOrderLineItem.to_json()

# convert the object into a dict
purchase_order_line_item_dict = purchase_order_line_item_instance.to_dict()
# create an instance of PurchaseOrderLineItem from a dict
purchase_order_line_item_form_dict = purchase_order_line_item.from_dict(purchase_order_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


