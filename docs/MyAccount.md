# MyAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement_invoicing_display_options** | **str** |  | 
**allow_expenses_entered_against_companies_flag** | **bool** |  | [optional] 
**allow_in_cell_entry_on_time_sheet** | **bool** |  | [optional] 
**authentication_service_type** | **str** |  | [optional] 
**auto_popup_quick_notes_with_stopwatch** | **bool** |  | [optional] 
**auto_start_stopwatch** | **bool** |  | [optional] 
**billable_forecast** | **float** |  | [optional] 
**calendar** | [**CalendarReference**](CalendarReference.md) |  | [optional] 
**calendar_sync_integration_flag** | **bool** |  | [optional] 
**client_id** | **str** |  | [optional] 
**company_activity_tab_format** | **str** |  | 
**copy_column_layouts_and_filters** | **bool** |  | [optional] 
**copy_pod_layouts** | **bool** |  | [optional] 
**copy_shared_default_views** | **bool** |  | [optional] 
**country** | [**CountryReference**](CountryReference.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**daily_capacity** | **float** |  | [optional] 
**days_tolerance** | **int** |  | [optional] 
**default_department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**default_email** | **str** |  | 
**default_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**default_phone** | **str** |  | 
**directional_sync** | [**DirectionalSyncReference**](DirectionalSyncReference.md) |  | [optional] 
**disable_online_flag** | **bool** |  | [optional] 
**employee_identifer** | **str** |  Max length: 10; | [optional] 
**enable_mobile_flag** | **bool** |  | [optional] 
**enable_mobile_gps_flag** | **bool** |  | [optional] 
**enter_time_against_company_flag** | **bool** |  | [optional] 
**expense_approver** | [**MemberReference**](MemberReference.md) |  | [optional] 
**first_name** | **str** |  Max length: 30; | 
**from_member_rec_id** | **int** |  | [optional] 
**global_search_default_sort** | **str** |  | [optional] 
**global_search_default_ticket_filter** | **str** |  | [optional] 
**hide_member_in_dispatch_portal_flag** | **bool** |  | [optional] 
**hire_date** | **datetime** |  | 
**home_email** | **str** |  Max length: 250; | [optional] 
**home_extension** | **str** |  Max length: 10; | [optional] 
**home_phone** | **str** |  Max length: 15; | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  Max length: 15; | 
**inactive_date** | **datetime** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**include_in_utilization_reporting_flag** | **bool** |  | [optional] 
**invoice_screen_default_tab_format** | **str** |  | 
**invoice_time_tab_format** | **str** |  | 
**invoicing_display_options** | **str** |  | 
**last_login** | **str** |  | [optional] 
**last_name** | **str** |  Max length: 30; | 
**license_class** | **str** | F &#x3D; Full Member, A &#x3D; API Member, C &#x3D; StreamlineIT Member, X &#x3D; Subcontractor Member | 
**mapi_name** | **str** |  | [optional] 
**member_personas** | **List[int]** |  | [optional] 
**middle_initial** | **str** |  Max length: 1; | [optional] 
**minimum_hours** | **float** |  | [optional] 
**mobile_email** | **str** |  Max length: 250; | [optional] 
**mobile_extension** | **str** |  Max length: 10; | [optional] 
**mobile_phone** | **str** |  Max length: 15; | [optional] 
**notes** | **str** |  | [optional] 
**office365** | [**MemberOffice365**](MemberOffice365.md) |  | [optional] 
**office_email** | **str** |  Max length: 250; | [optional] 
**office_extension** | **str** |  Max length: 10; | [optional] 
**office_phone** | **str** |  Max length: 15; | [optional] 
**partner_portal_flag** | **bool** |  | [optional] 
**password** | **str** | ConditionallyRequired. API Member will get random password generated Max length: 60; | [optional] 
**phone_integration_type** | **str** |  | [optional] 
**phone_source** | **str** |  | [optional] 
**photo** | [**DocumentReference**](DocumentReference.md) |  | [optional] 
**primary_email** | **str** |  Max length: 250; | [optional] 
**project_default_board** | [**ProjectBoardReference**](ProjectBoardReference.md) |  | [optional] 
**project_default_department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**project_default_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**report_card** | [**ReportCardReference**](ReportCardReference.md) |  | [optional] 
**reports_to** | [**MemberReference**](MemberReference.md) |  | [optional] 
**require_expense_entry_flag** | **bool** |  | [optional] 
**require_start_and_end_time_on_time_entry_flag** | **bool** |  | [optional] 
**require_time_sheet_entry_flag** | **bool** |  | [optional] 
**sales_default_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**schedule_capacity** | **float** |  | [optional] 
**schedule_default_department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**schedule_default_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**service_board_team_ids** | **List[int]** |  | [optional] 
**service_default_board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**service_default_department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**service_default_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**service_location** | [**ServiceLocationReference**](ServiceLocationReference.md) |  | [optional] 
**signature** | **str** |  | [optional] 
**sts_user_admin_url** | **str** |  | [optional] 
**time_approver** | [**MemberReference**](MemberReference.md) |  | [optional] 
**time_reminder_email_flag** | **bool** |  | [optional] 
**time_sheet_start_date** | **datetime** |  | [optional] 
**time_zone** | [**TimeZoneSetupReference**](TimeZoneSetupReference.md) |  | [optional] 
**timebased_one_time_password_activated** | **bool** |  | [optional] 
**title** | **str** |  Max length: 50; | [optional] 
**toast_notification_flag** | **bool** |  | [optional] 
**token** | **str** |  | [optional] 
**type** | [**MemberTypeReference**](MemberTypeReference.md) |  | [optional] 
**use_browser_language_flag** | **bool** |  | [optional] 
**vendor_number** | **str** |  | [optional] 
**warehouse** | [**WarehouseReference**](WarehouseReference.md) |  | [optional] 
**warehouse_bin** | [**WarehouseBinReference**](WarehouseBinReference.md) |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 
**work_type** | [**WorkTypeReference**](WorkTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.my_account import MyAccount

# TODO update the JSON string below
json = "{}"
# create an instance of MyAccount from a JSON string
my_account_instance = MyAccount.from_json(json)
# print the JSON string representation of the object
print MyAccount.to_json()

# convert the object into a dict
my_account_dict = my_account_instance.to_dict()
# create an instance of MyAccount from a dict
my_account_form_dict = my_account.from_dict(my_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


