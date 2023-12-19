# ProductPickingShippingDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**line_number** | **int** |  | [optional] 
**picked_quantity** | **int** |  | [optional] 
**product_item** | [**ProductItemReference**](ProductItemReference.md) |  | [optional] 
**quantity** | **int** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**serial_number_ids** | **List[int]** |  | [optional] 
**shipment_method** | [**ShipmentMethodReference**](ShipmentMethodReference.md) |  | [optional] 
**shipped_quantity** | **int** |  | [optional] 
**tracking_number** | **str** |  | [optional] 
**warehouse** | [**WarehouseReference**](WarehouseReference.md) |  | [optional] 
**warehouse_bin** | [**WarehouseBinReference**](WarehouseBinReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.product_picking_shipping_detail import ProductPickingShippingDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ProductPickingShippingDetail from a JSON string
product_picking_shipping_detail_instance = ProductPickingShippingDetail.from_json(json)
# print the JSON string representation of the object
print ProductPickingShippingDetail.to_json()

# convert the object into a dict
product_picking_shipping_detail_dict = product_picking_shipping_detail_instance.to_dict()
# create an instance of ProductPickingShippingDetail from a dict
product_picking_shipping_detail_form_dict = product_picking_shipping_detail.from_dict(product_picking_shipping_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


