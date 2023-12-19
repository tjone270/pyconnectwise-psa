# CatalogInventory


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
from connectwise_psa.models.catalog_inventory import CatalogInventory

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogInventory from a JSON string
catalog_inventory_instance = CatalogInventory.from_json(json)
# print the JSON string representation of the object
print CatalogInventory.to_json()

# convert the object into a dict
catalog_inventory_dict = catalog_inventory_instance.to_dict()
# create an instance of CatalogInventory from a dict
catalog_inventory_form_dict = catalog_inventory.from_dict(catalog_inventory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


