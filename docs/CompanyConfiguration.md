# CompanyConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**active_flag** | **bool** |  | [optional] 
**backup_billable_space_gb** | **float** |  | [optional] 
**backup_failed** | **int** |  | [optional] 
**backup_incomplete** | **int** |  | [optional] 
**backup_month** | **int** |  | [optional] 
**backup_protected_device_list** | **str** |  | [optional] 
**backup_restores** | **int** |  | [optional] 
**backup_server_name** | **str** |  Max length: 50; | [optional] 
**backup_successes** | **int** |  | [optional] 
**backup_year** | **int** |  | [optional] 
**bill_flag** | **bool** |  | [optional] 
**business_unit_id** | **int** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**company_location_id** | **int** |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**cpu_speed** | **str** |  Max length: 100; | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**default_gateway** | **str** |  Max length: 50; | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**device_identifier** | **str** |  Max length: 100; | [optional] 
**display_vendor_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**installation_date** | **datetime** |  | [optional] 
**installed_by** | [**MemberReference**](MemberReference.md) |  | [optional] 
**ip_address** | **str** |  Max length: 50; | [optional] 
**last_backup_date** | **datetime** |  | [optional] 
**last_login_name** | **str** |  Max length: 100; | [optional] 
**local_hard_drives** | **str** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**location_id** | **int** |  | [optional] 
**mac_address** | **str** |  Max length: 25; | [optional] 
**management_link** | **str** |  Max length: 1000; | [optional] 
**manufacturer** | [**ManufacturerReference**](ManufacturerReference.md) |  | [optional] 
**manufacturer_part_number** | **str** |  Max length: 50; | [optional] 
**mobile_guid** | **str** |  | [optional] 
**model_number** | **str** |  Max length: 50; | [optional] 
**name** | **str** |  Max length: 100; | 
**needs_renewal_flag** | **bool** |  | [optional] 
**notes** | **str** |  | [optional] 
**os_info** | **str** |  Max length: 250; | [optional] 
**os_type** | **str** |  Max length: 250; | [optional] 
**parent_configuration_id** | **int** |  | [optional] 
**purchase_date** | **datetime** |  | [optional] 
**questions** | [**List[ConfigurationQuestion]**](ConfigurationQuestion.md) |  | [optional] 
**ram** | **str** |  Max length: 25; | [optional] 
**remote_link** | **str** |  Max length: 1000; | [optional] 
**serial_number** | **str** |  Max length: 250; | [optional] 
**show_automate_flag** | **bool** |  | [optional] 
**show_remote_flag** | **bool** |  | [optional] 
**site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**sla** | [**SLAReference**](SLAReference.md) |  | [optional] 
**status** | [**ConfigurationStatusReference**](ConfigurationStatusReference.md) |  | [optional] 
**tag_number** | **str** |  Max length: 50; | [optional] 
**type** | [**ConfigurationTypeReference**](ConfigurationTypeReference.md) |  | [optional] 
**vendor** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**vendor_notes** | **str** |  | [optional] 
**warranty_expiration_date** | **datetime** |  | [optional] 

## Example

```python
from connectwise_psa.models.company_configuration import CompanyConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyConfiguration from a JSON string
company_configuration_instance = CompanyConfiguration.from_json(json)
# print the JSON string representation of the object
print CompanyConfiguration.to_json()

# convert the object into a dict
company_configuration_dict = company_configuration_instance.to_dict()
# create an instance of CompanyConfiguration from a dict
company_configuration_form_dict = company_configuration.from_dict(company_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


