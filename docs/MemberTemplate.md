# MemberTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**admin_flag** | **bool** |  | [optional] 
**agreement_invoicing_display_options** | **str** |  | [optional] 
**allow_expenses_entered_against_companies_flag** | **bool** |  | [optional] 
**allow_in_cell_entry_on_time_sheet** | **bool** |  | [optional] 
**auto_popup_quick_notes_with_stopwatch** | **bool** |  | [optional] 
**auto_start_stopwatch** | **bool** |  | [optional] 
**billable_forecast** | **float** |  | [optional] 
**calendar** | [**CalendarReference**](CalendarReference.md) |  | [optional] 
**company_activity_tab_format** | **str** |  | [optional] 
**copy_column_layouts_and_filters** | **bool** |  | [optional] 
**copy_pod_layouts** | **bool** |  | [optional] 
**copy_shared_default_views** | **bool** |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**daily_capacity** | **float** |  | [optional] 
**days_tolerance** | **int** |  | [optional] 
**default_department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**default_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**enable_mobile_flag** | **bool** |  | [optional] 
**enter_time_against_company_flag** | **bool** |  | [optional] 
**excluded_project_board_ids** | **List[int]** |  | [optional] 
**excluded_service_board_ids** | **List[int]** |  | [optional] 
**expense_approver** | [**MemberReference**](MemberReference.md) |  | [optional] 
**from_member_rec_id** | **int** |  | [optional] 
**from_member_template_rec_id** | **int** |  | [optional] 
**global_search_default_sort** | **str** |  | [optional] 
**global_search_default_ticket_filter** | **str** |  | [optional] 
**hide_member_in_dispatch_portal_flag** | **bool** |  | [optional] 
**hourly_cost** | **float** |  | [optional] 
**hourly_rate** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  Max length: 50; | 
**include_in_utilization_reporting_flag** | **bool** |  | [optional] 
**invoice_screen_default_tab_format** | **str** |  | [optional] 
**invoice_time_tab_format** | **str** |  | [optional] 
**invoicing_display_options** | **str** |  | [optional] 
**member_personas** | **List[int]** |  | [optional] 
**minimum_hours** | **float** |  | [optional] 
**partner_portal_flag** | **bool** |  | [optional] 
**phone_source** | **str** |  | [optional] 
**project_default_board** | [**ProjectBoardReference**](ProjectBoardReference.md) |  | [optional] 
**project_default_department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**project_default_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**report_card** | [**ReportCardReference**](ReportCardReference.md) |  | [optional] 
**reports_to** | [**MemberReference**](MemberReference.md) |  | [optional] 
**require_expense_entry_flag** | **bool** |  | [optional] 
**require_start_and_end_time_on_time_entry_flag** | **bool** |  | [optional] 
**require_time_sheet_entry_flag** | **bool** |  | [optional] 
**restrict_default_sales_territory_flag** | **bool** |  | [optional] 
**restrict_default_warehouse_bin_flag** | **bool** |  | [optional] 
**restrict_default_warehouse_flag** | **bool** |  | [optional] 
**restrict_department_flag** | **bool** |  | [optional] 
**restrict_location_flag** | **bool** |  | [optional] 
**restrict_project_default_department_flag** | **bool** |  | [optional] 
**restrict_project_default_location_flag** | **bool** |  | [optional] 
**restrict_schedule_flag** | **bool** |  | [optional] 
**restrict_service_default_department_flag** | **bool** |  | [optional] 
**restrict_service_default_location_flag** | **bool** |  | [optional] 
**sales_default_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**schedule_capacity** | **float** |  | [optional] 
**schedule_default_department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**schedule_default_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**security_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**service_board_team_ids** | **List[int]** |  | [optional] 
**service_default_board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**service_default_department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**service_default_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**service_location** | [**ServiceLocationReference**](ServiceLocationReference.md) |  | [optional] 
**structure_level** | [**StructureReference**](StructureReference.md) |  | [optional] 
**sts_user_admin_url** | **str** |  | [optional] 
**teams** | **List[int]** |  | [optional] 
**template_description** | **str** |  Max length: 1024; | [optional] 
**time_approver** | [**MemberReference**](MemberReference.md) |  | [optional] 
**time_reminder_email_flag** | **bool** |  | [optional] 
**time_sheet_start_date** | **str** |  | [optional] 
**time_zone** | [**TimeZoneSetupReference**](TimeZoneSetupReference.md) |  | [optional] 
**title** | **str** |  | [optional] 
**toast_notification_flag** | **bool** |  | [optional] 
**type** | [**MemberTypeReference**](MemberTypeReference.md) |  | [optional] 
**warehouse** | [**WarehouseReference**](WarehouseReference.md) |  | [optional] 
**warehouse_bin** | [**WarehouseBinReference**](WarehouseBinReference.md) |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 
**work_type** | [**WorkTypeReference**](WorkTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.member_template import MemberTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of MemberTemplate from a JSON string
member_template_instance = MemberTemplate.from_json(json)
# print the JSON string representation of the object
print MemberTemplate.to_json()

# convert the object into a dict
member_template_dict = member_template_instance.to_dict()
# create an instance of MemberTemplate from a dict
member_template_form_dict = member_template.from_dict(member_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


