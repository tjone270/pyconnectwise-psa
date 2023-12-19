# MyMember


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**admin_flag** | **bool** |  | [optional] 
**agreement_invoicing_display_options** | **str** |  | [optional] 
**allow_expenses_entered_against_companies_flag** | **bool** |  | [optional] 
**allow_in_cell_entry_on_time_sheet** | **bool** |  | [optional] 
**authentication_service_type** | **str** |  | [optional] 
**billable_forecast** | **float** |  | [optional] 
**calendar** | [**CalendarReference**](CalendarReference.md) |  | [optional] 
**calendar_sync_integration_flag** | **bool** |  | [optional] 
**company_activity_tab_format** | **str** |  | [optional] 
**corelytics_password** | **str** |  | [optional] 
**corelytics_username** | **str** |  | [optional] 
**country** | [**CountryReference**](CountryReference.md) |  | [optional] 
**daily_capacity** | **float** |  | [optional] 
**days_tolerance** | **int** |  | [optional] 
**default_department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**default_email** | **str** |  | [optional] 
**default_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**default_phone** | **str** |  | [optional] 
**directional_sync** | [**DirectionalSyncReference**](DirectionalSyncReference.md) |  | [optional] 
**disable_online_flag** | **bool** |  | [optional] 
**employee_identifer** | **str** |  | [optional] 
**enable_ldap_authentication_flag** | **bool** |  | [optional] 
**enable_mobile_flag** | **bool** |  | [optional] 
**enable_mobile_gps_flag** | **bool** |  | [optional] 
**enter_time_against_company_flag** | **bool** |  | [optional] 
**excluded_project_board_ids** | **List[int]** |  | [optional] 
**excluded_service_board_ids** | **List[int]** |  | [optional] 
**expense_approver** | [**MemberReference**](MemberReference.md) |  | [optional] 
**first_name** | **str** |  | [optional] 
**hide_member_in_dispatch_portal_flag** | **bool** |  | [optional] 
**hire_date** | **str** |  | [optional] 
**home_email** | **str** |  | [optional] 
**home_extension** | **str** |  | [optional] 
**home_phone** | **str** |  | [optional] 
**hourly_cost** | **float** |  | [optional] 
**hourly_rate** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**inactive_date** | **str** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**include_in_utilization_reporting_flag** | **bool** |  | [optional] 
**invoice_screen_default_tab_format** | **str** |  | [optional] 
**invoice_time_tab_format** | **str** |  | [optional] 
**invoicing_display_options** | **str** |  | [optional] 
**last_login** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**ldap_configuration** | [**LdapConfigurationReference**](LdapConfigurationReference.md) |  | [optional] 
**ldap_user_name** | **str** |  | [optional] 
**license_class** | **str** | F &#x3D; Full Member, A &#x3D; API Member, C &#x3D; StreamlineIT Member, X &#x3D; Subcontractor Member | [optional] 
**mapi_name** | **str** |  | [optional] 
**middle_initial** | **str** |  | [optional] 
**minimum_hours** | **float** |  | [optional] 
**mobile_email** | **str** |  | [optional] 
**mobile_extension** | **str** |  | [optional] 
**mobile_phone** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**office_email** | **str** |  | [optional] 
**office_extension** | **str** |  | [optional] 
**office_phone** | **str** |  | [optional] 
**password** | **str** | ConditionallyRequired. API Member will get random password generated | [optional] 
**photo** | [**DocumentReference**](DocumentReference.md) |  | [optional] 
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
**security_role** | [**SecurityRoleReference**](SecurityRoleReference.md) |  | [optional] 
**service_board_team_ids** | **List[int]** |  | [optional] 
**service_default_board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**service_default_department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**service_default_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**service_location** | [**ServiceLocationReference**](ServiceLocationReference.md) |  | [optional] 
**sso_client_id** | **str** |  | [optional] 
**sso_session_flag** | **bool** |  | [optional] 
**structure_level** | [**StructureReference**](StructureReference.md) |  | [optional] 
**time_approver** | [**MemberReference**](MemberReference.md) |  | [optional] 
**time_reminder_email_flag** | **bool** |  | [optional] 
**time_sheet_start_date** | **str** |  | [optional] 
**time_zone** | [**TimeZoneSetupReference**](TimeZoneSetupReference.md) |  | [optional] 
**timebased_one_time_password_activated** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**toast_notification_flag** | **bool** |  | [optional] 
**type** | [**MemberTypeReference**](MemberTypeReference.md) |  | [optional] 
**vendor_number** | **str** |  | [optional] 
**warehouse** | [**WarehouseReference**](WarehouseReference.md) |  | [optional] 
**warehouse_bin** | [**WarehouseBinReference**](WarehouseBinReference.md) |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 
**work_type** | [**WorkTypeReference**](WorkTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.my_member import MyMember

# TODO update the JSON string below
json = "{}"
# create an instance of MyMember from a JSON string
my_member_instance = MyMember.from_json(json)
# print the JSON string representation of the object
print MyMember.to_json()

# convert the object into a dict
my_member_dict = my_member_instance.to_dict()
# create an instance of MyMember from a dict
my_member_form_dict = my_member.from_dict(my_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


