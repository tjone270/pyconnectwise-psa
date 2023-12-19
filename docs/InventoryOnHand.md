# InventoryOnHand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**catalog_item** | [**CatalogItemReference**](CatalogItemReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**on_hand** | **int** |  | [optional] 
**serial_numbers** | [**List[OnHandSerialNumberReference]**](OnHandSerialNumberReference.md) |  | [optional] 
**warehouse** | [**WarehouseReference**](WarehouseReference.md) |  | [optional] 
**warehouse_bin** | [**WarehouseBinReference**](WarehouseBinReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.inventory_on_hand import InventoryOnHand

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryOnHand from a JSON string
inventory_on_hand_instance = InventoryOnHand.from_json(json)
# print the JSON string representation of the object
print InventoryOnHand.to_json()

# convert the object into a dict
inventory_on_hand_dict = inventory_on_hand_instance.to_dict()
# create an instance of InventoryOnHand from a dict
inventory_on_hand_form_dict = inventory_on_hand.from_dict(inventory_on_hand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


