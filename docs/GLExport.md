# GLExport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustment_transactions** | [**List[GLExportAdjustmentTransaction]**](GLExportAdjustmentTransaction.md) |  | [optional] 
**customers** | [**List[GLExportCustomer]**](GLExportCustomer.md) |  | [optional] 
**expense_bills** | [**List[GLExportExpenseBill]**](GLExportExpenseBill.md) |  | [optional] 
**expenses** | [**List[GLExportExpense]**](GLExportExpense.md) |  | [optional] 
**export_settings** | **object** |  | [optional] 
**inventory_transfers** | [**List[GLExportInventoryTransfer]**](GLExportInventoryTransfer.md) |  | [optional] 
**purchase_transactions** | [**List[GLExportPurchaseTransaction]**](GLExportPurchaseTransaction.md) |  | [optional] 
**transactions** | [**List[GLExportTransaction]**](GLExportTransaction.md) |  | [optional] 
**vendors** | [**List[GLExportVendor]**](GLExportVendor.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.gl_export import GLExport

# TODO update the JSON string below
json = "{}"
# create an instance of GLExport from a JSON string
gl_export_instance = GLExport.from_json(json)
# print the JSON string representation of the object
print GLExport.to_json()

# convert the object into a dict
gl_export_dict = gl_export_instance.to_dict()
# create an instance of GLExport from a dict
gl_export_form_dict = gl_export.from_dict(gl_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


