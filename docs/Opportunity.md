# Opportunity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**bill_to_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**bill_to_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**bill_to_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**billing_terms** | [**BillingTermsReference**](BillingTermsReference.md) |  | [optional] 
**business_unit_id** | **int** |  Required On Updates; | [optional] 
**campaign** | [**CampaignReference**](CampaignReference.md) |  | [optional] 
**closed_by** | [**MemberReference**](MemberReference.md) |  | [optional] 
**closed_date** | **datetime** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**company_location_id** | **int** |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**customer_po** | **str** |  Max length: 25; | [optional] 
**date_became_lead** | **datetime** |  | [optional] 
**expected_close_date** | **datetime** |  Required On Updates; | [optional] 
**id** | **int** |  | [optional] 
**location_id** | **int** |  Required On Updates; | [optional] 
**name** | **str** |  Max length: 100; | 
**notes** | **str** |  | [optional] 
**pipeline_change_date** | **datetime** |  | [optional] 
**primary_sales_rep** | [**MemberReference**](MemberReference.md) |  | [optional] 
**priority** | [**OpportunityPriorityReference**](OpportunityPriorityReference.md) |  | [optional] 
**probability** | [**OpportunityProbabilityReference**](OpportunityProbabilityReference.md) |  | [optional] 
**rating** | [**OpportunityRatingReference**](OpportunityRatingReference.md) |  | [optional] 
**secondary_sales_rep** | [**MemberReference**](MemberReference.md) |  | [optional] 
**ship_to_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**ship_to_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**ship_to_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**source** | **str** |  Max length: 50; | [optional] 
**stage** | [**OpportunityStageReference**](OpportunityStageReference.md) |  | [optional] 
**status** | [**OpportunityStatusReference**](OpportunityStatusReference.md) |  | [optional] 
**tax_code** | [**TaxCodeReference**](TaxCodeReference.md) |  | [optional] 
**technical_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**total_sales_tax** | **float** |  | [optional] 
**type** | [**OpportunityTypeReference**](OpportunityTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.opportunity import Opportunity

# TODO update the JSON string below
json = "{}"
# create an instance of Opportunity from a JSON string
opportunity_instance = Opportunity.from_json(json)
# print the JSON string representation of the object
print Opportunity.to_json()

# convert the object into a dict
opportunity_dict = opportunity_instance.to_dict()
# create an instance of Opportunity from a dict
opportunity_form_dict = opportunity.from_dict(opportunity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


