# Company


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**account_number** | **str** |  | [optional] 
**address_line1** | **str** | Gets or sets at least one address field is required -- addressLine1, addressLine2, city, state, zip and/or country. Max length: 50; | [optional] 
**address_line2** | **str** | Gets or sets at least one address field is required -- addressLine1, addressLine2, city, state, zip and/or country. Max length: 50; | [optional] 
**annual_revenue** | **float** |  | [optional] 
**bill_to_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**billing_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**billing_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**billing_terms** | [**BillingTermsReference**](BillingTermsReference.md) |  | [optional] 
**calendar** | [**CalendarReference**](CalendarReference.md) |  | [optional] 
**city** | **str** | Gets or sets at least one address field is required -- addressLine1, addressLine2, city, state, zip and/or country. Max length: 50; | [optional] 
**company_entity_type** | [**EntityTypeReference**](EntityTypeReference.md) |  | [optional] 
**country** | [**CountryReference**](CountryReference.md) |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**date_acquired** | **datetime** |  | [optional] 
**date_deleted** | **datetime** |  | [optional] 
**default_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**deleted_by** | **str** |  | [optional] 
**deleted_flag** | **bool** |  | [optional] 
**facebook_url** | **str** |  | [optional] 
**fax_number** | **str** |  Max length: 30; | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  Max length: 30; | 
**integrator_tags** | **List[str]** |  | [optional] 
**invoice_cc_email_address** | **str** |  | [optional] 
**invoice_delivery_method** | [**BillingDeliveryReference**](BillingDeliveryReference.md) |  | [optional] 
**invoice_template** | [**InvoiceTemplateReference**](InvoiceTemplateReference.md) |  | [optional] 
**invoice_to_email_address** | **str** |  | [optional] 
**is_vendor_flag** | **bool** |  | [optional] 
**lead_flag** | **bool** |  | [optional] 
**lead_source** | **str** |  Max length: 50; | [optional] 
**linked_in_url** | **str** |  | [optional] 
**market** | [**MarketDescriptionReference**](MarketDescriptionReference.md) |  | [optional] 
**mobile_guid** | **str** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**number_of_employees** | **int** |  | [optional] 
**ownership_type** | [**OwnershipTypeReference**](OwnershipTypeReference.md) |  | [optional] 
**parent_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**phone_number** | **str** |  Max length: 30; | [optional] 
**pricing_schedule** | [**PricingScheduleReference**](PricingScheduleReference.md) |  | [optional] 
**reseller_identifier** | **str** |  | [optional] 
**revenue_year** | **int** |  | [optional] 
**sic_code** | [**SicCodeReference**](SicCodeReference.md) |  | [optional] 
**site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**state** | **str** | Gets or sets at least one address field is required -- addressLine1, addressLine2, city, state, zip and/or country. Max length: 50; | [optional] 
**status** | [**CompanyStatusReference**](CompanyStatusReference.md) |  | [optional] 
**tax_code** | [**TaxCodeReference**](TaxCodeReference.md) |  | [optional] 
**tax_identifier** | **str** |  | [optional] 
**territory** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**territory_manager** | [**MemberReference**](MemberReference.md) |  | [optional] 
**time_zone_setup** | [**TimeZoneSetupReference**](TimeZoneSetupReference.md) |  | [optional] 
**twitter_url** | **str** |  | [optional] 
**types** | [**List[CompanyTypeReference]**](CompanyTypeReference.md) | Gets or sets integrer array of Company_Type_Recids to be assigned to company that can be passed in only during new company creation (post)             To update existing companies type, use the /company/companyTypeAssociations or /company/companies/{ID}/typeAssociations endpoints. | [optional] 
**unsubscribe_flag** | **bool** |  | [optional] 
**user_defined_field1** | **str** |  Max length: 50; | [optional] 
**user_defined_field10** | **str** |  Max length: 50; | [optional] 
**user_defined_field2** | **str** |  Max length: 50; | [optional] 
**user_defined_field3** | **str** |  Max length: 50; | [optional] 
**user_defined_field4** | **str** |  Max length: 50; | [optional] 
**user_defined_field5** | **str** |  Max length: 50; | [optional] 
**user_defined_field6** | **str** |  Max length: 50; | [optional] 
**user_defined_field7** | **str** |  Max length: 50; | [optional] 
**user_defined_field8** | **str** |  Max length: 50; | [optional] 
**user_defined_field9** | **str** |  Max length: 50; | [optional] 
**vendor_identifier** | **str** |  | [optional] 
**website** | **str** |  Max length: 255; | [optional] 
**year_established** | **int** |  | [optional] 
**zip** | **str** | Gets or sets at least one address field is required -- addressLine1, addressLine2, city, state, zip and/or country. Max length: 12; | [optional] 

## Example

```python
from connectwise_psa.models.company import Company

# TODO update the JSON string below
json = "{}"
# create an instance of Company from a JSON string
company_instance = Company.from_json(json)
# print the JSON string representation of the object
print Company.to_json()

# convert the object into a dict
company_dict = company_instance.to_dict()
# create an instance of Company from a dict
company_form_dict = company.from_dict(company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


