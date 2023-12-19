# PortalConfigurationServiceSetup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**actual_hours_flag** | **bool** |  | [optional] 
**approval_status_flag** | **bool** |  | [optional] 
**assigned_resources_flag** | **bool** |  | [optional] 
**budget_hours_flag** | **bool** |  | [optional] 
**closed_tasks_flag** | **bool** |  | [optional] 
**contact_flag** | **bool** |  | [optional] 
**display_closed_tickets_option** | **str** |  | 
**enable_chat_assist_flag** | **bool** |  | [optional] 
**entered_date_flag** | **bool** |  | [optional] 
**fixed_fee_ticket_template** | [**ServiceSignoffReference**](ServiceSignoffReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**last_update_flag** | **bool** |  | [optional] 
**open_tasks_flag** | **bool** |  | [optional] 
**required_date_flag** | **bool** |  | [optional] 
**service_board_flag** | **bool** |  | [optional] 
**service_sub_type_flag** | **bool** |  | [optional] 
**service_sub_type_item_flag** | **bool** |  | [optional] 
**service_type_flag** | **bool** |  | [optional] 
**site_name_flag** | **bool** |  | [optional] 
**sla_info_flag** | **bool** |  | [optional] 
**status_flag** | **bool** |  | [optional] 
**time_materials_ticket_template** | [**ServiceSignoffReference**](ServiceSignoffReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.portal_configuration_service_setup import PortalConfigurationServiceSetup

# TODO update the JSON string below
json = "{}"
# create an instance of PortalConfigurationServiceSetup from a JSON string
portal_configuration_service_setup_instance = PortalConfigurationServiceSetup.from_json(json)
# print the JSON string representation of the object
print PortalConfigurationServiceSetup.to_json()

# convert the object into a dict
portal_configuration_service_setup_dict = portal_configuration_service_setup_instance.to_dict()
# create an instance of PortalConfigurationServiceSetup from a dict
portal_configuration_service_setup_form_dict = portal_configuration_service_setup.from_dict(portal_configuration_service_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


