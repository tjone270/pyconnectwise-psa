# PortalConfigurationProjectSetup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**billing_method_flag** | **bool** |  | [optional] 
**contact_flag** | **bool** |  | [optional] 
**description_flag** | **bool** |  | [optional] 
**estimated_end_flag** | **bool** |  | [optional] 
**estimated_start_flag** | **bool** |  | [optional] 
**fixed_fee_actual_finish_flag** | **bool** |  | [optional] 
**fixed_fee_actual_hrs_flag** | **bool** |  | [optional] 
**fixed_fee_actual_start_flag** | **bool** |  | [optional] 
**fixed_fee_assigned_flag** | **bool** |  | [optional] 
**fixed_fee_bill_flag** | **bool** |  | [optional] 
**fixed_fee_budget_hrs_flag** | **bool** |  | [optional] 
**fixed_fee_scheduled_finish_flag** | **bool** |  | [optional] 
**fixed_fee_scheduled_hrs_flag** | **bool** |  | [optional] 
**fixed_fee_scheduled_start_flag** | **bool** |  | [optional] 
**fixed_fee_status_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**last_updated_flag** | **bool** |  | [optional] 
**only_display** | **str** |  | 
**portal_config** | [**PortalConfigurationReference**](PortalConfigurationReference.md) |  | [optional] 
**project_detail_total_hours_flag** | **bool** |  | [optional] 
**project_issue_actual_finish_flag** | **bool** |  | [optional] 
**project_issue_actual_hrs_flag** | **bool** |  | [optional] 
**project_issue_actual_start_flag** | **bool** |  | [optional] 
**project_issue_assigned_flag** | **bool** |  | [optional] 
**project_issue_bill_flag** | **bool** |  | [optional] 
**project_issue_budget_hrs_flag** | **bool** |  | [optional] 
**project_issue_scheduled_finish_flag** | **bool** |  | [optional] 
**project_issue_scheduled_hrs_flag** | **bool** |  | [optional] 
**project_issue_scheduled_start_flag** | **bool** |  | [optional] 
**project_issue_status_flag** | **bool** |  | [optional] 
**project_manager_flag** | **bool** |  | [optional] 
**project_name_flag** | **bool** |  | [optional] 
**project_type_flag** | **bool** |  | [optional] 
**status_flag** | **bool** |  | [optional] 
**time_material_actual_finish_flag** | **bool** |  | [optional] 
**time_material_actual_hrs_flag** | **bool** |  | [optional] 
**time_material_actual_start_flag** | **bool** |  | [optional] 
**time_material_assigned_flag** | **bool** |  | [optional] 
**time_material_bill_flag** | **bool** |  | [optional] 
**time_material_budget_hrs_flag** | **bool** |  | [optional] 
**time_material_scheduled_finish_flag** | **bool** |  | [optional] 
**time_material_scheduled_hrs_flag** | **bool** |  | [optional] 
**time_material_scheduled_start_flag** | **bool** |  | [optional] 
**time_material_status_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.portal_configuration_project_setup import PortalConfigurationProjectSetup

# TODO update the JSON string below
json = "{}"
# create an instance of PortalConfigurationProjectSetup from a JSON string
portal_configuration_project_setup_instance = PortalConfigurationProjectSetup.from_json(json)
# print the JSON string representation of the object
print PortalConfigurationProjectSetup.to_json()

# convert the object into a dict
portal_configuration_project_setup_dict = portal_configuration_project_setup_instance.to_dict()
# create an instance of PortalConfigurationProjectSetup from a dict
portal_configuration_project_setup_form_dict = portal_configuration_project_setup.from_dict(portal_configuration_project_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


