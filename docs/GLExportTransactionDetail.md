# GLExportTransactionDetail


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
**document_type** | **str** |  | [optional] 
**drop_shipped_flag** | **bool** |  | [optional] 
**gl_class** | **str** |  | [optional] 
**gl_item_id** | **str** |  | [optional] 
**gl_type_id** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**inventory_account_number** | **str** |  | [optional] 
**inventory_xref** | **str** |  | [optional] 
**invoice_summary_option** | **str** |  | [optional] 
**item** | [**IvItemReference**](IvItemReference.md) |  | [optional] 
**item_cost** | **float** |  | [optional] 
**item_description** | **str** |  | [optional] 
**item_price** | **float** |  | [optional] 
**item_taxable_flag** | **bool** |  | [optional] 
**item_type_xref** | **str** |  | [optional] 
**location_xref** | **str** |  | [optional] 
**memo** | **str** |  | [optional] 
**price_level_xref** | **str** |  | [optional] 
**product** | [**ProductReference**](ProductReference.md) |  | [optional] 
**product_account_number** | **str** |  | [optional] 
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
**tax_levels** | [**List[GLExportTransactionDetailTaxLevel]**](GLExportTransactionDetailTaxLevel.md) |  | [optional] 
**tax_note** | **str** |  | [optional] 
**tax_rate** | **float** |  | [optional] 
**tax_rate_percent** | **float** |  | [optional] 
**taxable2_flag** | **bool** |  | [optional] 
**taxable3_flag** | **bool** |  | [optional] 
**taxable4_flag** | **bool** |  | [optional] 
**taxable5_flag** | **bool** |  | [optional] 
**taxable_flag** | **bool** |  | [optional] 
**time_entry** | [**TimeEntryReference**](TimeEntryReference.md) |  | [optional] 
**total** | **float** |  | [optional] 
**unit_of_measure** | [**UnitOfMeasureReference**](UnitOfMeasureReference.md) |  | [optional] 
**uom_schedule_xref** | **str** |  | [optional] 
**warehouse_bin** | [**WarehouseBinReference**](WarehouseBinReference.md) |  | [optional] 
**warehouse_site** | [**SiteReference**](SiteReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.gl_export_transaction_detail import GLExportTransactionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of GLExportTransactionDetail from a JSON string
gl_export_transaction_detail_instance = GLExportTransactionDetail.from_json(json)
# print the JSON string representation of the object
print GLExportTransactionDetail.to_json()

# convert the object into a dict
gl_export_transaction_detail_dict = gl_export_transaction_detail_instance.to_dict()
# create an instance of GLExportTransactionDetail from a dict
gl_export_transaction_detail_form_dict = gl_export_transaction_detail.from_dict(gl_export_transaction_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


