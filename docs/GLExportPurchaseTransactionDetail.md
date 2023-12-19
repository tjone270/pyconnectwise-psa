# GLExportPurchaseTransactionDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**cogs_xref** | **str** |  | [optional] 
**cost** | **float** |  | [optional] 
**cost_account_number** | **str** |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**description** | **str** |  | [optional] 
**document_date** | **str** |  | [optional] 
**drop_shipped_flag** | **bool** |  | [optional] 
**gl_class** | **str** |  | [optional] 
**gl_item_id** | **str** |  | [optional] 
**gl_type_id** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**inventory_account_number** | **str** |  | [optional] 
**inventory_xref** | **str** |  | [optional] 
**item** | [**IvItemReference**](IvItemReference.md) |  | [optional] 
**item_cost** | **float** |  | [optional] 
**item_description** | **str** |  | [optional] 
**item_price** | **float** |  | [optional] 
**item_type_xref** | **str** |  | [optional] 
**line_number** | **int** |  | [optional] 
**location_xref** | **str** |  | [optional] 
**memo** | **str** |  | [optional] 
**price_level_xref** | **str** |  | [optional] 
**purchase_header_tax_group** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 
**sales_code** | **str** |  | [optional] 
**sales_description** | **str** |  | [optional] 
**serial_numbers** | **str** |  | [optional] 
**serialized_flag** | **bool** |  | [optional] 
**shipment_method** | [**ShipmentMethodReference**](ShipmentMethodReference.md) |  | [optional] 
**sub_category** | [**ProductSubCategoryReference**](ProductSubCategoryReference.md) |  | [optional] 
**tax_agency_xref** | **str** |  | [optional] 
**tax_code** | [**TaxCodeReference**](TaxCodeReference.md) |  | [optional] 
**tax_code_xref** | **str** |  | [optional] 
**tax_note** | **str** |  | [optional] 
**tax_rate** | **float** |  | [optional] 
**taxable** | **bool** |  | [optional] 
**total** | **float** |  | [optional] 
**unit_of_measure** | [**UnitOfMeasureReference**](UnitOfMeasureReference.md) |  | [optional] 
**uom_schedule_xref** | **str** |  | [optional] 
**vendor_account_number** | **str** |  | [optional] 
**vendor_number** | **str** |  | [optional] 
**warehouse_bin** | [**WarehouseBinReference**](WarehouseBinReference.md) |  | [optional] 
**warehouse_site** | [**SiteReference**](SiteReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.gl_export_purchase_transaction_detail import GLExportPurchaseTransactionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of GLExportPurchaseTransactionDetail from a JSON string
gl_export_purchase_transaction_detail_instance = GLExportPurchaseTransactionDetail.from_json(json)
# print the JSON string representation of the object
print GLExportPurchaseTransactionDetail.to_json()

# convert the object into a dict
gl_export_purchase_transaction_detail_dict = gl_export_purchase_transaction_detail_instance.to_dict()
# create an instance of GLExportPurchaseTransactionDetail from a dict
gl_export_purchase_transaction_detail_form_dict = gl_export_purchase_transaction_detail.from_dict(gl_export_purchase_transaction_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


