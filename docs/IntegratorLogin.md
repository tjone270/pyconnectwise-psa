# IntegratorLogin


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**activity_api_flag** | **bool** |  | [optional] 
**activity_callback_url** | **str** |  Max length: 1000; | [optional] 
**activity_legacy_callback_flag** | **bool** |  | [optional] 
**agreement_api_flag** | **bool** |  | [optional] 
**agreement_callback_legacy_flag** | **bool** |  | [optional] 
**agreement_callback_url** | **str** |  Max length: 1000; | [optional] 
**board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**can_access_all_apis_flag** | **bool** | Setting this flag to true will create an integrator that can access all of the available apis in the system.             If this field is set to true, both the member and board fields are required. | [optional] 
**can_access_all_records_flag** | **bool** | This flag controls whether the integrator can access only the db records it created, or all system records. | [optional] 
**company_api_flag** | **bool** |  | [optional] 
**company_callback_url** | **str** |  Max length: 1000; | [optional] 
**company_legacy_callback_flag** | **bool** |  | [optional] 
**configuration_api_flag** | **bool** |  | [optional] 
**configuration_auto_child_flag** | **bool** |  | [optional] 
**configuration_callback_url** | **str** |  Max length: 1000; | [optional] 
**configuration_childling_flag** | **bool** | True if integrator is allowed to child configurations. | [optional] 
**configuration_legacy_callback_flag** | **bool** |  | [optional] 
**contact_api_flag** | **bool** |  | [optional] 
**contact_callback_url** | **str** |  Max length: 1000; | [optional] 
**contact_legacy_callback_flag** | **bool** |  | [optional] 
**date_inactivated** | **datetime** |  | [optional] 
**document_api_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactivated_by** | [**MemberReference**](MemberReference.md) |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**invoice_api_flag** | **bool** |  | [optional] 
**managed_services_api_flag** | **bool** |  | [optional] 
**managed_services_auto_child_flag** | **bool** |  | [optional] 
**managed_services_childing_flag** | **bool** | True if integrator is allowed to child configurations. | [optional] 
**marketing_api_flag** | **bool** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**member_api_flag** | **bool** |  | [optional] 
**opportunity_api_flag** | **bool** |  | [optional] 
**opportunity_callback_url** | **str** |  Max length: 1000; | [optional] 
**opportunity_conversion_api_flag** | **bool** | True if the member has access to the Opportunity Conversion Api. | [optional] 
**opportunity_legacy_callback_flag** | **bool** |  | [optional] 
**password** | **str** | The password will never be returned in response. Max length: 50; | [optional] 
**product_api_flag** | **bool** |  | [optional] 
**product_callback_url** | **str** |  Max length: 1000; | [optional] 
**product_legacy_callback_flag** | **bool** |  | [optional] 
**project_api_flag** | **bool** |  | [optional] 
**project_callback_url** | **str** |  Max length: 1000; | [optional] 
**project_legacy_callback_flag** | **bool** |  | [optional] 
**purchasing_api_flag** | **bool** |  | [optional] 
**purchasing_callback_url** | **str** |  Max length: 1000; | [optional] 
**purchasing_legacy_callback_flag** | **bool** |  | [optional] 
**reporting_api_flag** | **bool** |  | [optional] 
**schedule_api_flag** | **bool** |  | [optional] 
**schedule_callback_url** | **str** |  Max length: 1000; | [optional] 
**schedule_legacy_callback_flag** | **bool** |  | [optional] 
**service_board_callback_url** | **str** |  Max length: 1000; | [optional] 
**service_board_legacy_callback_flag** | **bool** |  | [optional] 
**service_ticket_api_flag** | **bool** |  | [optional] 
**system_api_flag** | **bool** |  | [optional] 
**time_entry_api_flag** | **bool** |  | [optional] 
**time_entry_callback_url** | **str** |  Max length: 1000; | [optional] 
**time_entry_legacy_callback_flag** | **bool** |  | [optional] 
**username** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.integrator_login import IntegratorLogin

# TODO update the JSON string below
json = "{}"
# create an instance of IntegratorLogin from a JSON string
integrator_login_instance = IntegratorLogin.from_json(json)
# print the JSON string representation of the object
print IntegratorLogin.to_json()

# convert the object into a dict
integrator_login_dict = integrator_login_instance.to_dict()
# create an instance of IntegratorLogin from a dict
integrator_login_form_dict = integrator_login.from_dict(integrator_login_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


