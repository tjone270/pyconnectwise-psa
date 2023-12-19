# PurchaseOrder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**business_unit_id** | **int** |  | [optional] 
**cancel_reason** | **str** |  | [optional] 
**closed_by** | **str** |  | [optional] 
**closed_flag** | **bool** | The closed flag can only be updated via updating the purchase order status to a closed/open status. | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**customer_city** | **str** |  | [optional] 
**customer_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**customer_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**customer_country** | [**CountryReference**](CountryReference.md) |  | [optional] 
**customer_extension** | **str** |  | [optional] 
**customer_name** | **str** |  | [optional] 
**customer_phone** | **str** |  | [optional] 
**customer_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**customer_site_name** | **str** |  | [optional] 
**customer_state** | **str** |  | [optional] 
**customer_street_line1** | **str** |  | [optional] 
**customer_street_line2** | **str** |  | [optional] 
**customer_zip** | **str** |  | [optional] 
**date_closed** | **datetime** |  | [optional] 
**drop_ship_customer_flag** | **bool** |  | [optional] 
**entered_by** | **str** |  | [optional] 
**freight_cost** | **float** |  | [optional] 
**freight_packing_slip** | **str** |  | [optional] 
**freight_tax_total** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**internal_notes** | **str** |  | [optional] 
**location_id** | **int** |  | [optional] 
**po_date** | **datetime** |  Required On Updates; | [optional] 
**po_number** | **str** |  Required On Updates; Max length: 50; | [optional] 
**sales_tax** | **float** |  | [optional] 
**shipment_date** | **datetime** |  | [optional] 
**shipment_method** | [**ShipmentMethodReference**](ShipmentMethodReference.md) |  | [optional] 
**shipping_instructions** | **str** |  | [optional] 
**status** | [**PurchaseOrderStatusReference**](PurchaseOrderStatusReference.md) |  | [optional] 
**sub_total** | **float** |  | [optional] 
**tax_code** | [**TaxCodeReference**](TaxCodeReference.md) |  | [optional] 
**tax_freight_flag** | **bool** |  | [optional] 
**tax_po_flag** | **bool** |  | [optional] 
**terms** | [**BillingTermsReference**](BillingTermsReference.md) |  | [optional] 
**total** | **float** |  | [optional] 
**tracking_number** | **str** |  Max length: 50; | [optional] 
**update_shipment_info** | **bool** | Determines whether or not to update all of the shipment info for each associated line item when new shipment info is passed in. | [optional] 
**update_vendor_order_number** | **bool** | Determines whether or not to update vendor order number for each associated line item when new vendor order number is passed in. | [optional] 
**vendor_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**vendor_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**vendor_invoice_date** | **datetime** |  | [optional] 
**vendor_invoice_number** | **str** |  Max length: 50; | [optional] 
**vendor_order_number** | **str** |  Max length: 50; | [optional] 
**vendor_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**warehouse** | [**WarehouseReference**](WarehouseReference.md) |  | [optional] 
**warehouse_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.purchase_order import PurchaseOrder

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrder from a JSON string
purchase_order_instance = PurchaseOrder.from_json(json)
# print the JSON string representation of the object
print PurchaseOrder.to_json()

# convert the object into a dict
purchase_order_dict = purchase_order_instance.to_dict()
# create an instance of PurchaseOrder from a dict
purchase_order_form_dict = purchase_order.from_dict(purchase_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


