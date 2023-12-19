# MemberDeactivation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**MemberDeactivationSalesActivity**](MemberDeactivationSalesActivity.md) |  | [optional] 
**company_team** | [**List[MemberDeactivationCompanyTeam]**](MemberDeactivationCompanyTeam.md) | A list of customers for which the member holds a team role | [optional] 
**delete_open_time_sheets_flag** | **bool** | By default, this is set to false             If there is any open timesheets, system will return error message             that there is open timesheets still attached to this member             If user would like to delete member with open timesheets, they can set this boolean to TRUE             System will delete member and any associated open timesheets | [optional] 
**department_manager** | [**MemberDeactivationDepartmentMananager**](MemberDeactivationDepartmentMananager.md) |  | [optional] 
**dispatch_member** | [**MemberDeactivationDispatchMember**](MemberDeactivationDispatchMember.md) |  | [optional] 
**duty_manager** | [**MemberDeactivationDutyManager**](MemberDeactivationDutyManager.md) |  | [optional] 
**knowledge_base_article** | [**MemberDeactivationKnowledgebaseArticle**](MemberDeactivationKnowledgebaseArticle.md) |  | [optional] 
**my_company_coo** | [**MemberDeactivationMyCompanyCOORole**](MemberDeactivationMyCompanyCOORole.md) |  | [optional] 
**my_company_controller** | [**MemberDeactivationMyCompanyControllerRole**](MemberDeactivationMyCompanyControllerRole.md) |  | [optional] 
**my_company_dispatch** | [**MemberDeactivationMyCompanyDispatchRole**](MemberDeactivationMyCompanyDispatchRole.md) |  | [optional] 
**my_company_duty_manager_role** | [**MemberDeactivationMyCompanyDutyManagerRole**](MemberDeactivationMyCompanyDutyManagerRole.md) |  | [optional] 
**my_company_president** | [**MemberDeactivationMyCompanyPresidentRole**](MemberDeactivationMyCompanyPresidentRole.md) |  | [optional] 
**my_company_service_manager** | [**MemberDeactivationMyCompanyServiceManagerRole**](MemberDeactivationMyCompanyServiceManagerRole.md) |  | [optional] 
**opportunity** | [**MemberDeactivationOpportunity**](MemberDeactivationOpportunity.md) |  | [optional] 
**project_expense_approver** | [**MemberDeactivationProjectManager**](MemberDeactivationProjectManager.md) |  | [optional] 
**project_manager** | [**MemberDeactivationProjectManager**](MemberDeactivationProjectManager.md) |  | [optional] 
**project_time_approver** | [**MemberDeactivationProjectManager**](MemberDeactivationProjectManager.md) |  | [optional] 
**sales_team** | [**MemberDeactivationSalesTeam**](MemberDeactivationSalesTeam.md) |  | [optional] 
**send_from_email_notify** | [**MemberDeactivationSendFromEmailNotify**](MemberDeactivationSendFromEmailNotify.md) |  | [optional] 
**service_manager** | [**MemberDeactivationServiceManger**](MemberDeactivationServiceManger.md) |  | [optional] 
**service_status_workflow** | [**List[MemberDeactivationStatusWorkflow]**](MemberDeactivationStatusWorkflow.md) |  | [optional] 
**service_team** | [**MemberDeactivationServiceTeam**](MemberDeactivationServiceTeam.md) |  | [optional] 
**ticket_template** | [**MemberDeactivationServiceTemplate**](MemberDeactivationServiceTemplate.md) |  | [optional] 
**workflow_email** | [**MemberDeactivationWorkflow**](MemberDeactivationWorkflow.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.member_deactivation import MemberDeactivation

# TODO update the JSON string below
json = "{}"
# create an instance of MemberDeactivation from a JSON string
member_deactivation_instance = MemberDeactivation.from_json(json)
# print the JSON string representation of the object
print MemberDeactivation.to_json()

# convert the object into a dict
member_deactivation_dict = member_deactivation_instance.to_dict()
# create an instance of MemberDeactivation from a dict
member_deactivation_form_dict = member_deactivation.from_dict(member_deactivation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


