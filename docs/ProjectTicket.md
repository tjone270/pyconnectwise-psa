# ProjectTicket


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**actual_hours** | **float** |  | [optional] 
**address_line1** | **str** |  Max length: 50; | [optional] 
**address_line2** | **str** |  Max length: 50; | [optional] 
**agreement** | [**AgreementReference**](AgreementReference.md) |  | [optional] 
**allow_all_clients_portal_view** | **bool** |  | [optional] 
**approved** | **bool** |  | [optional] 
**automatic_email_cc** | **str** |  Max length: 1000; | [optional] 
**automatic_email_cc_flag** | **bool** |  | [optional] 
**automatic_email_contact_flag** | **bool** |  | [optional] 
**automatic_email_resource_flag** | **bool** |  | [optional] 
**bill_expenses** | **str** |  | [optional] 
**bill_products** | **str** |  | [optional] 
**bill_time** | **str** |  | [optional] 
**board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**budget_hours** | **float** |  | [optional] 
**city** | **str** |  Max length: 50; | [optional] 
**closed_by** | **str** |  | [optional] 
**closed_date** | **str** |  | [optional] 
**closed_flag** | **bool** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**contact_email_address** | **str** |  Max length: 250; | [optional] 
**contact_email_lookup** | **str** |  | [optional] 
**contact_name** | **str** |  Max length: 62; | [optional] 
**contact_phone_extension** | **str** |  Max length: 15; | [optional] 
**contact_phone_number** | **str** |  Max length: 20; | [optional] 
**country** | [**CountryReference**](CountryReference.md) |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**customer_updated_flag** | **bool** |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**duration** | **int** |  | [optional] 
**estimated_start_date** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**initial_description** | **str** | Only available for POST, will not be returned in the response. | [optional] 
**initial_internal_analysis** | **str** | Only available for POST, will not be returned in the response. | [optional] 
**initial_resolution** | **str** | Only available for POST, will not be returned in the response. | [optional] 
**is_issue_flag** | **bool** |  | [optional] 
**item** | [**ServiceItemReference**](ServiceItemReference.md) |  | [optional] 
**knowledge_base_category_id** | **int** |  | [optional] 
**knowledge_base_link_id** | **int** |  | [optional] 
**knowledge_base_link_type** | **str** |  | [optional] 
**knowledge_base_sub_category_id** | **int** |  | [optional] 
**lag_days** | **int** |  | [optional] 
**lag_nonworking_days_flag** | **bool** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**mobile_guid** | **str** |  | [optional] 
**opportunity** | [**OpportunityReference**](OpportunityReference.md) |  | [optional] 
**owner** | [**MemberReference**](MemberReference.md) |  | [optional] 
**phase** | [**ProjectPhaseReference**](ProjectPhaseReference.md) |  | [optional] 
**predecessor_closed_flag** | **bool** |  | [optional] 
**predecessor_id** | **int** |  | [optional] 
**predecessor_type** | **str** |  | [optional] 
**priority** | [**PriorityReference**](PriorityReference.md) |  | [optional] 
**process_notifications** | **bool** | Can be set to false to skip notification processing when adding or updating a ticket (Defaults to True). | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**required_date** | **datetime** |  | [optional] 
**resources** | **str** |  | [optional] 
**service_location** | [**ServiceLocationReference**](ServiceLocationReference.md) |  | [optional] 
**site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**site_name** | **str** |  Max length: 50; | [optional] 
**skip_callback** | **bool** |  | [optional] 
**source** | [**ServiceSourceReference**](ServiceSourceReference.md) |  | [optional] 
**state_identifier** | **str** |  Max length: 50; | [optional] 
**status** | [**ServiceStatusReference**](ServiceStatusReference.md) |  | [optional] 
**sub_billing_amount** | **float** |  | [optional] 
**sub_billing_method** | **str** |  | [optional] 
**sub_date_accepted** | **str** |  | [optional] 
**sub_type** | [**ServiceSubTypeReference**](ServiceSubTypeReference.md) |  | [optional] 
**summary** | **str** |  Max length: 100; | 
**tasks** | [**List[TicketTask]**](TicketTask.md) |  | [optional] 
**type** | [**ServiceTypeReference**](ServiceTypeReference.md) |  | [optional] 
**wbs_code** | **str** |  Max length: 50; | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 
**work_type** | [**WorkTypeReference**](WorkTypeReference.md) |  | [optional] 
**zip** | **str** |  Max length: 12; | [optional] 

## Example

```python
from connectwise_psa.models.project_ticket import ProjectTicket

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTicket from a JSON string
project_ticket_instance = ProjectTicket.from_json(json)
# print the JSON string representation of the object
print ProjectTicket.to_json()

# convert the object into a dict
project_ticket_dict = project_ticket_instance.to_dict()
# create an instance of ProjectTicket from a dict
project_ticket_form_dict = project_ticket.from_dict(project_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


