# RmaTag


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**account_manager** | [**MemberReference**](MemberReference.md) |  | [optional] 
**closed_by** | [**MemberReference**](MemberReference.md) |  | [optional] 
**closing_notes** | **str** |  Max length: 1000; | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**date_closed** | **str** |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**drop_ship_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**internal_notes** | **str** |  Max length: 1000; | [optional] 
**invoice** | [**InvoiceReference**](InvoiceReference.md) |  | [optional] 
**iv_description** | **str** |  | [optional] 
**list_price** | **float** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**mfg_item_id** | **str** |  Max length: 100; | [optional] 
**problem_description** | **str** |  Max length: 1000; | [optional] 
**product** | [**IvItemReference**](IvItemReference.md) |  | [optional] 
**product_description** | **str** |  Max length: 200; | 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**purchased_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**purchased_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**purchased_contact_address_line1** | **str** |  Max length: 50; | [optional] 
**purchased_contact_address_line2** | **str** |  Max length: 50; | [optional] 
**purchased_contact_city** | **str** |  Max length: 50; | [optional] 
**purchased_contact_country** | [**CountryReference**](CountryReference.md) |  | [optional] 
**purchased_contact_email** | **str** |  | [optional] 
**purchased_contact_extension** | **str** |  | [optional] 
**purchased_contact_phone** | **str** |  | [optional] 
**purchased_contact_state** | **str** |  Max length: 50; | [optional] 
**purchased_contact_type** | **str** |  | [optional] 
**purchased_contact_zip** | **str** |  Max length: 12; | [optional] 
**purchased_invoice_date** | **date** |  | [optional] 
**purchased_invoice_number** | **str** |  Max length: 50; | [optional] 
**purchased_notes** | **str** |  Max length: 1000; | [optional] 
**purchased_order_number** | **str** |  Max length: 50; | [optional] 
**purchased_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**purchased_vendor_action** | [**RmaActionReference**](RmaActionReference.md) |  | [optional] 
**purchased_vendor_rma_number** | **str** |  Max length: 50; | [optional] 
**repair_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**repair_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**repair_contact_address_line1** | **str** |  Max length: 50; | [optional] 
**repair_contact_address_line2** | **str** |  Max length: 50; | [optional] 
**repair_contact_city** | **str** |  Max length: 50; | [optional] 
**repair_contact_country** | [**CountryReference**](CountryReference.md) |  | [optional] 
**repair_contact_email** | **str** |  | [optional] 
**repair_contact_extension** | **str** |  | [optional] 
**repair_contact_phone** | **str** |  | [optional] 
**repair_contact_state** | **str** |  Max length: 50; | [optional] 
**repair_contact_type** | **str** |  | [optional] 
**repair_contact_zip** | **str** |  Max length: 12; | [optional] 
**repair_notes** | **str** |  Max length: 1000; | [optional] 
**repair_order_number** | **str** |  Max length: 50; | [optional] 
**repair_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**returned_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**returned_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**returned_contact_address_line1** | **str** |  Max length: 50; | [optional] 
**returned_contact_address_line2** | **str** |  Max length: 50; | [optional] 
**returned_contact_city** | **str** |  Max length: 50; | [optional] 
**returned_contact_country** | [**CountryReference**](CountryReference.md) |  | [optional] 
**returned_contact_email** | **str** |  | [optional] 
**returned_contact_extension** | **str** |  | [optional] 
**returned_contact_phone** | **str** |  | [optional] 
**returned_contact_state** | **str** |  Max length: 50; | [optional] 
**returned_contact_type** | **str** |  | [optional] 
**returned_contact_zip** | **str** |  Max length: 12; | [optional] 
**returned_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**rma_disposition** | [**RmaDispositionReference**](RmaDispositionReference.md) |  | [optional] 
**sales_order** | [**SalesOrderReference**](SalesOrderReference.md) |  | [optional] 
**serial_number** | **str** |  | [optional] 
**service_ticket** | [**TicketReference**](TicketReference.md) |  | [optional] 
**ship_method** | [**ShipmentMethodReference**](ShipmentMethodReference.md) |  | [optional] 
**shipping_date** | **date** |  | [optional] 
**shipping_tracking_number** | **str** |  Max length: 50; | [optional] 
**status** | [**RmaStatusReference**](RmaStatusReference.md) |  | [optional] 
**summary** | **str** |  Max length: 150; | [optional] 
**technical_contact** | [**MemberReference**](MemberReference.md) |  | [optional] 
**unit_price** | **float** |  | [optional] 
**warranty_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**warranty_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**warranty_contact_address_line1** | **str** |  Max length: 50; | [optional] 
**warranty_contact_address_line2** | **str** |  Max length: 50; | [optional] 
**warranty_contact_city** | **str** |  Max length: 50; | [optional] 
**warranty_contact_country** | [**CountryReference**](CountryReference.md) |  | [optional] 
**warranty_contact_email** | **str** |  | [optional] 
**warranty_contact_extension** | **str** |  | [optional] 
**warranty_contact_phone** | **str** |  | [optional] 
**warranty_contact_state** | **str** |  Max length: 50; | [optional] 
**warranty_contact_type** | **str** |  | [optional] 
**warranty_contact_zip** | **str** |  Max length: 12; | [optional] 
**warranty_notes** | **str** |  Max length: 1000; | [optional] 
**warranty_site** | [**SiteReference**](SiteReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.rma_tag import RmaTag

# TODO update the JSON string below
json = "{}"
# create an instance of RmaTag from a JSON string
rma_tag_instance = RmaTag.from_json(json)
# print the JSON string representation of the object
print RmaTag.to_json()

# convert the object into a dict
rma_tag_dict = rma_tag_instance.to_dict()
# create an instance of RmaTag from a dict
rma_tag_form_dict = rma_tag.from_dict(rma_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


