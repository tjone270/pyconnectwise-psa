# WorkflowAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**activity_status** | [**ActivityStatusReference**](ActivityStatusReference.md) |  | [optional] 
**activity_type** | [**ActivityTypeReference**](ActivityTypeReference.md) |  | [optional] 
**attach_configurations_for** | **str** | Required when notifyType is set to: \&quot;Attach Configuration\&quot; | [optional] 
**attached_track** | [**TrackReference**](TrackReference.md) |  | [optional] 
**attachments** | **List[int]** |  | [optional] 
**audit_notes_flag** | **bool** |  | [optional] 
**automate_script** | [**AutomateScriptReference**](AutomateScriptReference.md) |  | [optional] 
**bcc_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**board_status** | [**ServiceStatusReference**](ServiceStatusReference.md) |  | [optional] 
**cc_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**company_status** | [**CompanyStatusReference**](CompanyStatusReference.md) |  | [optional] 
**configuration_status** | [**ConfigurationStatusReference**](ConfigurationStatusReference.md) |  | [optional] 
**configuration_type** | [**ConfigurationTypeReference**](ConfigurationTypeReference.md) |  | [optional] 
**days_to_execute** | **int** |  | [optional] 
**detail_notes_flag** | **bool** |  | [optional] 
**email_from** | **str** | Required when notifyFrom is set to: \&quot;Email Address\&quot; Max length: 250; | [optional] 
**email_recipient** | **str** | Required when notifyWho is set to: \&quot;Email Address\&quot; Max length: 250; | [optional] 
**group** | [**GroupReference**](GroupReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**internal_notes_flag** | **bool** |  | [optional] 
**invoice_min_days** | **int** |  | [optional] 
**notes** | **str** |  | [optional] 
**notify_from** | [**NotificationRecipientReference**](NotificationRecipientReference.md) |  | [optional] 
**notify_type** | [**NotifyTypeReference**](NotifyTypeReference.md) |  | 
**notify_who** | [**NotificationRecipientReference**](NotificationRecipientReference.md) |  | [optional] 
**project_status** | [**ProjectStatusReference**](ProjectStatusReference.md) |  | [optional] 
**sales_order_status** | [**OrderStatusReference**](OrderStatusReference.md) |  | [optional] 
**script_fail_status** | [**ServiceStatusReference**](ServiceStatusReference.md) |  | [optional] 
**script_success_status** | [**ServiceStatusReference**](ServiceStatusReference.md) |  | [optional] 
**service_item** | [**ServiceItemReference**](ServiceItemReference.md) |  | [optional] 
**service_priority** | [**PriorityReference**](PriorityReference.md) |  | [optional] 
**service_sub_type** | [**ServiceSubTypeReference**](ServiceSubTypeReference.md) |  | [optional] 
**service_survey** | [**ServiceSurveyReference**](ServiceSurveyReference.md) |  | [optional] 
**service_template** | [**ServiceTemplateReference**](ServiceTemplateReference.md) |  | [optional] 
**service_type** | [**ServiceTypeReference**](ServiceTypeReference.md) |  | [optional] 
**specific_member_from** | [**MemberReference**](MemberReference.md) |  | [optional] 
**specific_member_to** | [**MemberReference**](MemberReference.md) |  | [optional] 
**specific_team_to** | [**GenericBoardTeamReference**](GenericBoardTeamReference.md) |  | [optional] 
**subject** | **str** | Required when notifyType is set to: \&quot;Create Activity\&quot;, \&quot;Send Email\&quot;, \&quot;Assign Resource\&quot; Max length: 100; | [optional] 
**update_owner_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.workflow_action import WorkflowAction

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowAction from a JSON string
workflow_action_instance = WorkflowAction.from_json(json)
# print the JSON string representation of the object
print WorkflowAction.to_json()

# convert the object into a dict
workflow_action_dict = workflow_action_instance.to_dict()
# create an instance of WorkflowAction from a dict
workflow_action_form_dict = workflow_action.from_dict(workflow_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


