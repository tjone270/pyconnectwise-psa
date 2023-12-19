# ProjectPhase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**actual_end** | **str** |  | [optional] 
**actual_hours** | **float** |  | [optional] 
**actual_start** | **str** |  | [optional] 
**agreement** | [**AgreementReference**](AgreementReference.md) |  | [optional] 
**bill_expenses** | **str** |  Required On Updates; | [optional] 
**bill_phase_closed_flag** | **bool** | This phase can only be billed after it has been closed. | [optional] 
**bill_products** | **str** |  Required On Updates; | [optional] 
**bill_project_closed_flag** | **bool** | This phase can only be billed after the project has been closed. | [optional] 
**bill_separately_flag** | **bool** |  | [optional] 
**bill_time** | **str** |  Required On Updates; | [optional] 
**bill_to_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**bill_to_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**bill_to_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**billing_method** | **str** | billingMethod is required if the phase billSeparatelyFlag is true. | [optional] 
**billing_start_date** | **datetime** |  | [optional] 
**board** | [**ProjectBoardReference**](ProjectBoardReference.md) |  | [optional] 
**budget_hours** | **float** |  | [optional] 
**business_unit_id** | **int** |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**deadline_date** | **datetime** |  | [optional] 
**description** | **str** |  Max length: 100; | 
**downpayment** | **float** |  | [optional] 
**estimated_expense_cost** | **float** |  | [optional] 
**estimated_expense_revenue** | **float** |  | [optional] 
**estimated_product_cost** | **float** |  | [optional] 
**estimated_product_revenue** | **float** |  | [optional] 
**estimated_time_cost** | **float** |  | [optional] 
**estimated_time_revenue** | **float** |  | [optional] 
**hourly_rate** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**location_id** | **int** |  | [optional] 
**mark_as_milestone_flag** | **bool** |  | [optional] 
**notes** | **str** |  | [optional] 
**opportunity** | [**OpportunityReference**](OpportunityReference.md) |  | [optional] 
**parent_phase** | [**ProjectPhaseReference**](ProjectPhaseReference.md) |  | [optional] 
**po_amount** | **float** |  | [optional] 
**po_number** | **str** |  Max length: 25; | [optional] 
**project_id** | **int** |  | [optional] 
**scheduled_end** | **str** |  | [optional] 
**scheduled_hours** | **float** |  | [optional] 
**scheduled_start** | **str** |  | [optional] 
**ship_to_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**ship_to_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**ship_to_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**status** | [**PhaseStatusReference**](PhaseStatusReference.md) |  | [optional] 
**wbs_code** | **str** |  Max length: 50; | [optional] 

## Example

```python
from connectwise_psa.models.project_phase import ProjectPhase

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPhase from a JSON string
project_phase_instance = ProjectPhase.from_json(json)
# print the JSON string representation of the object
print ProjectPhase.to_json()

# convert the object into a dict
project_phase_dict = project_phase_instance.to_dict()
# create an instance of ProjectPhase from a dict
project_phase_form_dict = project_phase.from_dict(project_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


