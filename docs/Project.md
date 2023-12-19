# Project


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**actual_end** | **datetime** |  | [optional] 
**actual_hours** | **float** |  | [optional] 
**actual_start** | **datetime** |  | [optional] 
**agreement** | [**AgreementReference**](AgreementReference.md) |  | [optional] 
**bill_expenses** | **str** |  Required On Updates; | [optional] 
**bill_products** | **str** |  Required On Updates; | [optional] 
**bill_project_after_closed_flag** | **bool** |  | [optional] 
**bill_time** | **str** |  Required On Updates; | [optional] 
**bill_to_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**bill_to_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**bill_to_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**bill_unapproved_time_and_expense** | **bool** |  | [optional] 
**billing_amount** | **float** |  | [optional] 
**billing_attention** | **str** |  Max length: 50; | [optional] 
**billing_method** | **str** |  | 
**billing_rate_type** | **str** |  Required On Updates; | [optional] 
**billing_start_date** | **datetime** |  | [optional] 
**billing_terms** | [**BillingTermsReference**](BillingTermsReference.md) |  | [optional] 
**board** | [**ProjectBoardReference**](ProjectBoardReference.md) |  | [optional] 
**budget_analysis** | **str** |  Required On Updates; | [optional] 
**budget_flag** | **bool** |  | [optional] 
**budget_hours** | **float** |  | [optional] 
**closed_flag** | **bool** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**company_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**customer_po** | **str** |  Max length: 50; | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**description** | **str** |  | [optional] 
**do_not_display_in_portal_flag** | **bool** |  | [optional] 
**downpayment** | **float** |  | [optional] 
**estimated_end** | **datetime** |  | 
**estimated_expense_cost** | **float** |  | [optional] 
**estimated_expense_revenue** | **float** |  | [optional] 
**estimated_hours** | **float** |  | [optional] 
**estimated_product_cost** | **float** |  | [optional] 
**estimated_product_revenue** | **float** |  | [optional] 
**estimated_start** | **datetime** |  | 
**estimated_time_cost** | **float** |  | [optional] 
**estimated_time_revenue** | **float** |  | [optional] 
**expense_approver** | [**MemberReference**](MemberReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**include_dependencies_flag** | **bool** |  | [optional] 
**include_estimates_flag** | **bool** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**manager** | [**MemberReference**](MemberReference.md) |  | [optional] 
**name** | **str** |  Max length: 100; | 
**opportunity** | [**OpportunityReference**](OpportunityReference.md) |  | [optional] 
**percent_complete** | **float** |  | [optional] 
**po_amount** | **float** |  | [optional] 
**project_template_id** | **int** |  | [optional] 
**restrict_down_payment_flag** | **bool** |  | [optional] 
**scheduled_end** | **datetime** |  | [optional] 
**scheduled_hours** | **float** |  | [optional] 
**scheduled_start** | **datetime** |  | [optional] 
**ship_to_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**ship_to_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**ship_to_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**status** | [**ProjectStatusReference**](ProjectStatusReference.md) |  | [optional] 
**tax_code** | [**TaxCodeReference**](TaxCodeReference.md) |  | [optional] 
**time_approver** | [**MemberReference**](MemberReference.md) |  | [optional] 
**type** | [**ProjectTypeReference**](ProjectTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print Project.to_json()

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_form_dict = project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


