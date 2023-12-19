# GLExportInventoryTransfer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**bin** | [**WarehouseBinReference**](WarehouseBinReference.md) |  | [optional] 
**cogs_xref** | **str** |  | [optional] 
**cost** | **float** |  | [optional] 
**cost_account_number** | **str** |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**description** | **str** |  | [optional] 
**document_date** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**gl_class** | **str** |  | [optional] 
**gl_item_id** | **str** |  | [optional] 
**gl_type_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**inventory_account_number** | **str** |  | [optional] 
**inventory_xref** | **str** |  | [optional] 
**item** | [**IvItemReference**](IvItemReference.md) |  | [optional] 
**item_description** | **str** |  | [optional] 
**item_price** | **float** |  | [optional] 
**item_type_xref** | **str** |  | [optional] 
**location_xref** | **str** |  | [optional] 
**memo** | **str** |  | [optional] 
**offset** | [**GLExportInventoryTransferOffset**](GLExportInventoryTransferOffset.md) |  | [optional] 
**price_level_xref** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 
**sales_code** | **str** |  | [optional] 
**sales_description** | **str** |  | [optional] 
**serial_numbers** | **str** |  | [optional] 
**serialized_flag** | **bool** |  | [optional] 
**sub_category** | [**ProductSubCategoryReference**](ProductSubCategoryReference.md) |  | [optional] 
**tax_note** | **str** |  | [optional] 
**taxable** | **bool** |  | [optional] 
**total** | **float** |  | [optional] 
**transfer_from_bin** | [**WarehouseBinReference**](WarehouseBinReference.md) |  | [optional] 
**transfer_from_location_xref** | **str** |  | [optional] 
**transfer_id** | **int** |  | [optional] 
**transfer_to_bin** | [**WarehouseBinReference**](WarehouseBinReference.md) |  | [optional] 
**transfer_to_location_xref** | **str** |  | [optional] 
**unit_of_measure** | [**UnitOfMeasureReference**](UnitOfMeasureReference.md) |  | [optional] 
**uom_schedule_xref** | **str** |  | [optional] 
**warehouse** | [**WarehouseReference**](WarehouseReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.gl_export_inventory_transfer import GLExportInventoryTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of GLExportInventoryTransfer from a JSON string
gl_export_inventory_transfer_instance = GLExportInventoryTransfer.from_json(json)
# print the JSON string representation of the object
print GLExportInventoryTransfer.to_json()

# convert the object into a dict
gl_export_inventory_transfer_dict = gl_export_inventory_transfer_instance.to_dict()
# create an instance of GLExportInventoryTransfer from a dict
gl_export_inventory_transfer_form_dict = gl_export_inventory_transfer.from_dict(gl_export_inventory_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


