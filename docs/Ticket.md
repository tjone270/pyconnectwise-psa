# Ticket


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
**billing_amount** | **float** |  | [optional] 
**billing_method** | **str** |  | [optional] 
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
**date_resolved** | **str** |  | [optional] 
**date_resplan** | **str** |  | [optional] 
**date_responded** | **str** |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**duration** | **int** |  | [optional] 
**escalation_level** | **int** |  | [optional] 
**escalation_start_date_utc** | **str** |  | [optional] 
**estimated_expense_cost** | **float** |  | [optional] 
**estimated_expense_revenue** | **float** |  | [optional] 
**estimated_product_cost** | **float** |  | [optional] 
**estimated_product_revenue** | **float** |  | [optional] 
**estimated_start_date** | **datetime** |  | [optional] 
**estimated_time_cost** | **float** |  | [optional] 
**estimated_time_revenue** | **float** |  | [optional] 
**external_x_ref** | **str** |  Max length: 100; | [optional] 
**has_child_ticket** | **bool** |  | [optional] 
**has_merged_child_ticket_flag** | **bool** |  | [optional] 
**hourly_rate** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**impact** | **str** |  Required On Updates; | [optional] 
**initial_description** | **str** | Only available for POST, will not be returned in the response. | [optional] 
**initial_description_from** | **str** |  | [optional] 
**initial_internal_analysis** | **str** | Only available for POST, will not be returned in the response. | [optional] 
**initial_resolution** | **str** | Only available for POST, will not be returned in the response. | [optional] 
**integrator_tags** | **List[str]** |  | [optional] 
**is_in_sla** | **bool** |  | [optional] 
**item** | [**ServiceItemReference**](ServiceItemReference.md) |  | [optional] 
**knowledge_base_category_id** | **int** |  | [optional] 
**knowledge_base_link_id** | **int** |  | [optional] 
**knowledge_base_link_type** | **str** |  | [optional] 
**knowledge_base_sub_category_id** | **int** |  | [optional] 
**lag_days** | **int** |  | [optional] 
**lag_nonworking_days_flag** | **bool** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**merged_parent_ticket** | [**TicketReference**](TicketReference.md) |  | [optional] 
**minutes_before_waiting** | **int** |  | [optional] 
**minutes_waiting** | **int** |  | [optional] 
**mobile_guid** | **str** |  | [optional] 
**opportunity** | [**OpportunityReference**](OpportunityReference.md) |  | [optional] 
**owner** | [**MemberReference**](MemberReference.md) |  | [optional] 
**parent_ticket_id** | **int** |  | [optional] 
**po_number** | **str** |  Max length: 50; | [optional] 
**predecessor_closed_flag** | **bool** |  | [optional] 
**predecessor_id** | **int** |  | [optional] 
**predecessor_type** | **str** |  | [optional] 
**priority** | [**PriorityReference**](PriorityReference.md) |  | [optional] 
**process_notifications** | **bool** | Can be set to false to skip notification processing when adding or updating a ticket (Defaults to True). | [optional] 
**record_type** | **str** |  | [optional] 
**request_for_change_flag** | **bool** |  | [optional] 
**required_date** | **datetime** |  | [optional] 
**res_plan_minutes** | **int** |  | [optional] 
**resolution_hours** | **float** |  | [optional] 
**resolve_minutes** | **int** |  | [optional] 
**resolved_by** | **str** |  | [optional] 
**resources** | **str** |  | [optional] 
**resplan_by** | **str** |  | [optional] 
**resplan_hours** | **float** |  | [optional] 
**resplan_skipped_minutes** | **int** |  | [optional] 
**respond_minutes** | **int** |  | [optional] 
**responded_by** | **str** |  | [optional] 
**responded_hours** | **float** |  | [optional] 
**responded_skipped_minutes** | **int** |  | [optional] 
**service_location** | [**ServiceLocationReference**](ServiceLocationReference.md) |  | [optional] 
**severity** | **str** |  Required On Updates; | [optional] 
**site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**site_name** | **str** |  Max length: 50; | [optional] 
**skip_callback** | **bool** |  | [optional] 
**sla** | [**SLAReference**](SLAReference.md) |  | [optional] 
**sla_status** | **str** |  | [optional] 
**source** | [**ServiceSourceReference**](ServiceSourceReference.md) |  | [optional] 
**state_identifier** | **str** |  Max length: 50; | [optional] 
**status** | [**ServiceStatusReference**](ServiceStatusReference.md) |  | [optional] 
**sub_billing_amount** | **float** |  | [optional] 
**sub_billing_method** | **str** |  | [optional] 
**sub_date_accepted** | **str** |  | [optional] 
**sub_type** | [**ServiceSubTypeReference**](ServiceSubTypeReference.md) |  | [optional] 
**summary** | **str** |  Max length: 100; | 
**team** | [**ServiceTeamReference**](ServiceTeamReference.md) |  | [optional] 
**type** | [**ServiceTypeReference**](ServiceTypeReference.md) |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 
**work_type** | [**WorkTypeReference**](WorkTypeReference.md) |  | [optional] 
**zip** | **str** |  Max length: 12; | [optional] 

## Example

```python
from connectwise_psa.models.ticket import Ticket

# TODO update the JSON string below
json = "{}"
# create an instance of Ticket from a JSON string
ticket_instance = Ticket.from_json(json)
# print the JSON string representation of the object
print Ticket.to_json()

# convert the object into a dict
ticket_dict = ticket_instance.to_dict()
# create an instance of Ticket from a dict
ticket_form_dict = ticket.from_dict(ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


