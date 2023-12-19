# Board


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**all_sort** | **str** |  | [optional] 
**auto_assign_limit_amount** | **int** | This field can only be set when autoAssignLimitFlag is true | [optional] 
**auto_assign_limit_flag** | **bool** |  | [optional] 
**auto_assign_new_ec_tickets_flag** | **bool** |  | [optional] 
**auto_assign_new_portal_tickets_flag** | **bool** |  | [optional] 
**auto_assign_new_tickets_flag** | **bool** |  | [optional] 
**auto_assign_ticket_owner_flag** | **bool** |  | [optional] 
**auto_close_status** | [**ServiceStatusReference**](ServiceStatusReference.md) |  | [optional] 
**bill_expense** | **str** |  | [optional] 
**bill_product** | **str** |  | [optional] 
**bill_ticket_separately_flag** | **bool** |  | [optional] 
**bill_tickets_after_closed_flag** | **bool** |  | [optional] 
**bill_time** | **str** |  | [optional] 
**bill_unapproved_time_expense_flag** | **bool** |  | [optional] 
**board_icon** | [**DocumentReference**](DocumentReference.md) |  | [optional] 
**closed_loop_all_flag** | **bool** |  | [optional] 
**closed_loop_discussions_flag** | **bool** |  | [optional] 
**closed_loop_internal_analysis_flag** | **bool** |  | [optional] 
**closed_loop_resolution_flag** | **bool** |  | [optional] 
**contact_template** | [**ServiceEmailTemplateReference**](ServiceEmailTemplateReference.md) |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**discussions_locked_flag** | **bool** |  | [optional] 
**dispatch_member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**duty_manager_member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**email_connector_allow_reopen_closed_flag** | **bool** |  | [optional] 
**email_connector_never_reopen_by_days_closed_flag** | **bool** | This field can only be set when emailConnectorAllowReopenClosed is true. | [optional] 
**email_connector_never_reopen_by_days_flag** | **bool** | This field can only be set when emailConnectorAllowReopenClosed is true. | [optional] 
**email_connector_new_ticket_no_match_flag** | **bool** | This field can only be set when emailConnectorAllowReopenClosed is true. | [optional] 
**email_connector_reopen_days_closed_limit** | **int** | This field can only be set when emailConnectorNeverReopenByDaysClosedFlag and emailConnectorAllowReopenClosed are both true             This field is required when emailConnectorNeverReopenByDaysClosedFlag is true. | [optional] 
**email_connector_reopen_days_limit** | **int** | This field can only be set when emailConnectorNeverReopenByDaysFlag and emailConnectorAllowReopenClosed are both true             This field is required when emailConnectorNeverReopenByDaysFlag is true. | [optional] 
**email_connector_reopen_resources_flag** | **bool** | This field can only be set when emailConnectorAllowReopenClosed is true. | [optional] 
**email_connector_reopen_status** | [**ServiceStatusReference**](ServiceStatusReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**internal_analysis_sort** | **str** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**mark_first_note_issue_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**notify_email_from** | **str** |  Max length: 50; | [optional] 
**notify_email_from_name** | **str** |  Max length: 60; | [optional] 
**oncall_member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**override_billing_setup_flag** | **bool** |  | [optional] 
**percentage_calculation** | **str** |  | [optional] 
**problem_sort** | **str** |  | [optional] 
**project_flag** | **bool** |  | [optional] 
**resolution_sort** | **str** |  | [optional] 
**resource_template** | [**ServiceEmailTemplateReference**](ServiceEmailTemplateReference.md) |  | [optional] 
**restrict_board_by_default_flag** | **bool** |  | [optional] 
**send_to_cc_flag** | **bool** |  | [optional] 
**send_to_contact_flag** | **bool** |  | [optional] 
**send_to_resource_flag** | **bool** |  | [optional] 
**service_manager_member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**show_dependencies_flag** | **bool** | This field only shows if it is Project Board. | [optional] 
**show_estimates_flag** | **bool** | This field only shows if it is Project Board. | [optional] 
**sign_off_template** | [**ServiceSignoffReference**](ServiceSignoffReference.md) |  | [optional] 
**time_entry_discussion_flag** | **bool** |  | [optional] 
**time_entry_internal_analysis_flag** | **bool** |  | [optional] 
**time_entry_locked_flag** | **bool** |  | [optional] 
**time_entry_resolution_flag** | **bool** |  | [optional] 
**use_member_display_name_flag** | **bool** |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 
**work_type** | [**WorkTypeReference**](WorkTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.board import Board

# TODO update the JSON string below
json = "{}"
# create an instance of Board from a JSON string
board_instance = Board.from_json(json)
# print the JSON string representation of the object
print Board.to_json()

# convert the object into a dict
board_dict = board_instance.to_dict()
# create an instance of Board from a dict
board_form_dict = board.from_dict(board_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


