# MyMemberInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**allow_expenses_entered_against_companies_flag** | **bool** |  | [optional] 
**daily_capacity** | **float** |  | [optional] 
**default_department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**default_email** | **str** |  | [optional] 
**default_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**enter_time_against_company_flag** | **bool** |  | [optional] 
**excluded_project_board_ids** | **List[int]** |  | [optional] 
**excluded_service_board_ids** | **List[int]** |  | [optional] 
**first_name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**last_name** | **str** |  | [optional] 
**license_class** | **str** | F &#x3D; Full Member, A &#x3D; API Member, C &#x3D; StreamlineIT Member, X &#x3D; Subcontractor Member | [optional] 
**middle_initial** | **str** |  | [optional] 
**photo** | [**DocumentReference**](DocumentReference.md) |  | [optional] 
**project_default_board** | [**ProjectBoardReference**](ProjectBoardReference.md) |  | [optional] 
**project_default_department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**project_default_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**require_expense_entry_flag** | **bool** |  | [optional] 
**require_start_and_end_time_on_time_entry_flag** | **bool** |  | [optional] 
**require_time_sheet_entry_flag** | **bool** |  | [optional] 
**restrict_default_warehouse_bin_flag** | **bool** |  | [optional] 
**restrict_default_warehouse_flag** | **bool** |  | [optional] 
**restrict_project_default_department_flag** | **bool** |  | [optional] 
**restrict_project_default_location_flag** | **bool** |  | [optional] 
**restrict_service_default_department_flag** | **bool** |  | [optional] 
**restrict_service_default_location_flag** | **bool** |  | [optional] 
**sales_default_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**schedule_capacity** | **float** |  | [optional] 
**schedule_default_department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**schedule_default_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**service_default_board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**service_default_department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**service_default_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**service_location** | [**ServiceLocationReference**](ServiceLocationReference.md) |  | [optional] 
**sso_client_id** | **str** |  | [optional] 
**sso_session_flag** | **bool** |  | [optional] 
**time_zone** | [**TimeZoneSetupReference**](TimeZoneSetupReference.md) |  | [optional] 
**use_browser_language_flag** | **bool** |  | [optional] 
**warehouse** | [**WarehouseReference**](WarehouseReference.md) |  | [optional] 
**warehouse_bin** | [**WarehouseBinReference**](WarehouseBinReference.md) |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 
**work_type** | [**WorkTypeReference**](WorkTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.my_member_info import MyMemberInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MyMemberInfo from a JSON string
my_member_info_instance = MyMemberInfo.from_json(json)
# print the JSON string representation of the object
print MyMemberInfo.to_json()

# convert the object into a dict
my_member_info_dict = my_member_info_instance.to_dict()
# create an instance of MyMemberInfo from a dict
my_member_info_form_dict = my_member_info.from_dict(my_member_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


