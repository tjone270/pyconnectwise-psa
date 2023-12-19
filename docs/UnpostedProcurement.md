# UnpostedProcurement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**avalara_tax_flag** | **bool** | Used to determine if Avalara tax is enabled. | [optional] 
**billing_terms** | [**BillingTermsReference**](BillingTermsReference.md) |  | [optional] 
**city_tax_amount** | **float** |  | [optional] 
**city_tax_flag** | **bool** | Set to true if transaction is taxable at the city level. | [optional] 
**city_tax_xref** | **str** |  | [optional] 
**composite_tax_amount** | **float** |  | [optional] 
**composite_tax_flag** | **bool** | Set to true if transaction is taxable at the composite level. | [optional] 
**composite_tax_xref** | **str** |  | [optional] 
**country_tax_amount** | **float** |  | [optional] 
**country_tax_flag** | **bool** | Set to true if transaction is taxable at the country level. | [optional] 
**country_tax_xref** | **str** |  | [optional] 
**county_tax_amount** | **float** |  | [optional] 
**county_tax_flag** | **bool** | Set to true if transaction is taxable at the county level. | [optional] 
**county_tax_xref** | **str** |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**customer** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**date_closed** | **str** |  | [optional] 
**department_id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**freight_cost** | **float** |  | [optional] 
**freight_tax_total** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**item_taxable_flag** | **bool** |  | [optional] 
**level_six_tax_amount** | **float** |  | [optional] 
**level_six_tax_flag** | **bool** | Set to true if transaction is taxable at level six. | [optional] 
**level_six_tax_xref** | **str** |  | [optional] 
**location_id** | **int** |  | [optional] 
**procurement_type** | **str** |  | [optional] 
**purchase_date** | **str** |  | [optional] 
**purchase_order** | [**PurchaseOrderReference**](PurchaseOrderReference.md) |  | [optional] 
**purchase_order_taxable_flag** | **bool** |  | [optional] 
**state_tax_amount** | **float** |  | [optional] 
**state_tax_flag** | **bool** | Set to true if transaction is taxable at the state level. | [optional] 
**state_tax_xref** | **str** |  | [optional] 
**tax_code** | [**TaxCodeReference**](TaxCodeReference.md) |  | [optional] 
**tax_freight_flag** | **bool** |  | [optional] 
**tax_total** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**tracking_number** | **str** |  | [optional] 
**unposted_product_id** | **str** |  | [optional] 
**vendor** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**vendor_account_number** | **str** |  | [optional] 
**vendor_invoice_date** | **str** |  | [optional] 
**vendor_invoice_number** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.unposted_procurement import UnpostedProcurement

# TODO update the JSON string below
json = "{}"
# create an instance of UnpostedProcurement from a JSON string
unposted_procurement_instance = UnpostedProcurement.from_json(json)
# print the JSON string representation of the object
print UnpostedProcurement.to_json()

# convert the object into a dict
unposted_procurement_dict = unposted_procurement_instance.to_dict()
# create an instance of UnpostedProcurement from a dict
unposted_procurement_form_dict = unposted_procurement.from_dict(unposted_procurement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


