# GLExportInventoryTransferOffset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**document_date** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**gl_class** | **str** |  | [optional] 
**gl_type_id** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**memo** | **str** |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.gl_export_inventory_transfer_offset import GLExportInventoryTransferOffset

# TODO update the JSON string below
json = "{}"
# create an instance of GLExportInventoryTransferOffset from a JSON string
gl_export_inventory_transfer_offset_instance = GLExportInventoryTransferOffset.from_json(json)
# print the JSON string representation of the object
print GLExportInventoryTransferOffset.to_json()

# convert the object into a dict
gl_export_inventory_transfer_offset_dict = gl_export_inventory_transfer_offset_instance.to_dict()
# create an instance of GLExportInventoryTransferOffset from a dict
gl_export_inventory_transfer_offset_form_dict = gl_export_inventory_transfer_offset.from_dict(gl_export_inventory_transfer_offset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


