# ProductItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**add_components_flag** | **bool** |  | [optional] 
**agreement** | [**AgreementReference**](AgreementReference.md) |  | [optional] 
**agreement_amount** | **float** |  | [optional] 
**billable_option** | **str** |  | 
**business_unit** | [**BillingUnitReference**](BillingUnitReference.md) |  | [optional] 
**business_unit_id** | **int** |  Required On Updates; | [optional] 
**bypass_forecast_update** | **bool** |  | [optional] 
**calculated_cost** | **float** |  | [optional] 
**calculated_cost_flag** | **bool** |  | [optional] 
**calculated_price** | **float** |  | [optional] 
**calculated_price_flag** | **bool** |  | [optional] 
**cancelled_by** | **int** |  | [optional] 
**cancelled_date** | **datetime** |  | [optional] 
**cancelled_flag** | **bool** |  | [optional] 
**cancelled_reason** | **str** |  Max length: 100; | [optional] 
**catalog_item** | [**CatalogItemReference**](CatalogItemReference.md) |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**cost** | **float** |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**customer_description** | **str** |  Max length: 6000; Required On Updates; | [optional] 
**description** | **str** |  Max length: 2000; | [optional] 
**discount** | **float** |  | [optional] 
**dropship_flag** | **bool** |  | [optional] 
**entity_type** | [**EntityTypeReference**](EntityTypeReference.md) |  | [optional] 
**forecast_detail_id** | **int** |  | [optional] 
**forecast_status** | [**OpportunityStatusReference**](OpportunityStatusReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**ignore_pricing_schedules_flag** | **bool** |  | [optional] 
**integration_x_ref** | **str** |  | [optional] 
**internal_notes** | **str** |  Max length: 1000; | [optional] 
**invoice** | [**InvoiceReference**](InvoiceReference.md) |  | [optional] 
**invoice_grouping** | [**InvoiceGroupingReference**](InvoiceGroupingReference.md) |  | [optional] 
**list_price** | **float** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**location_id** | **int** |  Required On Updates; | [optional] 
**minimum_stock_flag** | **bool** |  | [optional] 
**need_to_order_quantity** | **int** |  | [optional] 
**need_to_purchase_flag** | **bool** |  | [optional] 
**opportunity** | [**OpportunityReference**](OpportunityReference.md) |  | [optional] 
**phase** | [**ProjectPhaseReference**](ProjectPhaseReference.md) |  | [optional] 
**phase_product_flag** | **bool** |  | [optional] 
**po_approved_flag** | **bool** |  | [optional] 
**price** | **float** |  | [optional] 
**price_method** | **str** |  | [optional] 
**product_class** | **str** |  | [optional] 
**product_supplied_flag** | **bool** |  | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**purchase_date** | **datetime** |  | [optional] 
**quantity** | **float** |  | [optional] 
**quantity_cancelled** | **float** |  | [optional] 
**recurring** | [**ProductRecurring**](ProductRecurring.md) |  | [optional] 
**sales_order** | [**SalesOrderReference**](SalesOrderReference.md) |  | [optional] 
**sequence_number** | **float** |  | [optional] 
**serial_number_ids** | **List[int]** |  | [optional] 
**serial_numbers** | **List[str]** |  | [optional] 
**ship_set** | **str** |  Max length: 10; | [optional] 
**sla** | [**SLAReference**](SLAReference.md) |  | [optional] 
**special_order_flag** | **bool** |  | [optional] 
**sub_contractor_amount_limit** | **float** |  | [optional] 
**sub_contractor_ship_to_id** | **int** |  | [optional] 
**taxable_flag** | **bool** |  | [optional] 
**ticket** | [**TicketReference**](TicketReference.md) |  | [optional] 
**vendor** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**vendor_sku** | **str** |  Max length: 50; | [optional] 
**warehouse** | **str** |  | [optional] 
**warehouse_bin** | **str** |  | [optional] 
**warehouse_bin_id** | **int** |  | [optional] 
**warehouse_bin_id_object** | [**WarehouseBinReference**](WarehouseBinReference.md) |  | [optional] 
**warehouse_id** | **int** |  | [optional] 
**warehouse_id_object** | [**WarehouseReference**](WarehouseReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.product_item import ProductItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProductItem from a JSON string
product_item_instance = ProductItem.from_json(json)
# print the JSON string representation of the object
print ProductItem.to_json()

# convert the object into a dict
product_item_dict = product_item_instance.to_dict()
# create an instance of ProductItem from a dict
product_item_form_dict = product_item.from_dict(product_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


