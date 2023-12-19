# CompanyManagementSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement** | [**AgreementReference**](AgreementReference.md) |  | [optional] 
**alerts_generated** | **str** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**cpu_utilization** | **float** |  | [optional] 
**device_type** | **str** | Gets or sets deviceType is required if the managementSolution is Legacy. | [optional] 
**disk_cleanups** | **int** |  | [optional] 
**disk_defragmentations** | **int** |  | [optional] 
**disk_space_cleaned_mb** | **int** |  | [optional] 
**failed_backup_jobs** | **int** |  | [optional] 
**fully_patched_machines** | **int** |  | [optional] 
**group_identifier** | **str** |  Max length: 100; | 
**id** | **int** |  | [optional] 
**internet_connectivity** | **float** |  | [optional] 
**management_solution** | [**ManagementSolutionReference**](ManagementSolutionReference.md) |  | [optional] 
**memory_utilization** | **float** |  | [optional] 
**missing_more_five_patches_machines** | **int** |  | [optional] 
**missing_one_two_patches_machines** | **int** |  | [optional] 
**missing_security_patches** | **str** |  | [optional] 
**missing_three_five_patches_machines** | **int** |  | [optional] 
**missing_unscanned_patches_machines** | **int** |  | [optional] 
**server_availability** | **int** |  | [optional] 
**servers_disk_space_low** | **int** |  | [optional] 
**servers_offline** | **int** |  | [optional] 
**snmp_machines** | **int** |  | [optional] 
**spyware_items_removed** | **int** |  | [optional] 
**successful_backup_jobs** | **int** |  | [optional] 
**total_managed_machines** | **int** |  | [optional] 
**total_notifications** | **int** |  | [optional] 
**total_servers** | **int** |  | [optional] 
**total_windows_servers** | **int** |  | [optional] 
**total_windows_workstations** | **int** |  | [optional] 
**total_workstations** | **int** |  | [optional] 
**viruses_removed** | **int** |  | [optional] 
**windows_patches_installed** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.company_management_summary import CompanyManagementSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyManagementSummary from a JSON string
company_management_summary_instance = CompanyManagementSummary.from_json(json)
# print the JSON string representation of the object
print CompanyManagementSummary.to_json()

# convert the object into a dict
company_management_summary_dict = company_management_summary_instance.to_dict()
# create an instance of CompanyManagementSummary from a dict
company_management_summary_form_dict = company_management_summary.from_dict(company_management_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


