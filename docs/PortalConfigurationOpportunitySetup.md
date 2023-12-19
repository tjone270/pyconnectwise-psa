# PortalConfigurationOpportunitySetup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**acceptance_change_status_flag** | **bool** |  | [optional] 
**acceptance_create_activity_flag** | **bool** |  | [optional] 
**acceptance_email_activity_type** | [**ActivityTypeReference**](ActivityTypeReference.md) |  | [optional] 
**acceptance_email_assigned_by_member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**acceptance_email_body** | **str** |  | [optional] 
**acceptance_email_from_first_name** | **str** |  | [optional] 
**acceptance_email_from_last_name** | **str** |  | [optional] 
**acceptance_email_subject** | **str** |  | [optional] 
**acceptance_from_email** | **str** | Gets or sets             required when acceptanceSendEmailFlag is true. | [optional] 
**acceptance_opportunity_status** | [**OpportunityStatusReference**](OpportunityStatusReference.md) |  | [optional] 
**acceptance_send_email_flag** | **bool** |  | [optional] 
**add_all_opportunity_statuses** | **bool** |  | [optional] 
**add_all_opportunity_types** | **bool** |  | [optional] 
**confirmation_email_body** | **str** |  | [optional] 
**confirmation_email_from_first_name** | **str** |  | [optional] 
**confirmation_email_from_last_name** | **str** |  | [optional] 
**confirmation_email_subject** | **str** |  | [optional] 
**confirmation_email_use_default_company_email_address_flag** | **bool** |  | [optional] 
**confirmation_from_email** | **str** | Gets or sets             required when confirmationSendEmailFlag is true. | [optional] 
**confirmation_send_email_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**opportunity_status_rec_ids** | **List[int]** |  | [optional] 
**opportunity_type_rec_ids** | **List[int]** |  | [optional] 
**rejection_change_status_flag** | **bool** |  | [optional] 
**rejection_create_activity_flag** | **bool** |  | [optional] 
**rejection_email_activity_type** | [**ActivityTypeReference**](ActivityTypeReference.md) |  | [optional] 
**rejection_email_assigned_by_member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**rejection_email_body** | **str** |  | [optional] 
**rejection_email_from_first_name** | **str** |  | [optional] 
**rejection_email_from_last_name** | **str** |  | [optional] 
**rejection_email_subject** | **str** |  | [optional] 
**rejection_from_email** | **str** | Gets or sets             required when rejectionSendEmailFlag is true. | [optional] 
**rejection_opportunity_status** | [**OpportunityStatusReference**](OpportunityStatusReference.md) |  | [optional] 
**rejection_send_email_flag** | **bool** |  | [optional] 
**remove_all_opportunity_statuses** | **bool** |  | [optional] 
**remove_all_opportunity_types** | **bool** |  | [optional] 
**restrict_view_by_opportunity_status_flag** | **bool** |  | [optional] 
**restrict_view_by_opportunity_type_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.portal_configuration_opportunity_setup import PortalConfigurationOpportunitySetup

# TODO update the JSON string below
json = "{}"
# create an instance of PortalConfigurationOpportunitySetup from a JSON string
portal_configuration_opportunity_setup_instance = PortalConfigurationOpportunitySetup.from_json(json)
# print the JSON string representation of the object
print PortalConfigurationOpportunitySetup.to_json()

# convert the object into a dict
portal_configuration_opportunity_setup_dict = portal_configuration_opportunity_setup_instance.to_dict()
# create an instance of PortalConfigurationOpportunitySetup from a dict
portal_configuration_opportunity_setup_form_dict = portal_configuration_opportunity_setup.from_dict(portal_configuration_opportunity_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


