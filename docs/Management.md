# Management


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**added_configuration_status** | [**ConfigurationStatusReference**](ConfigurationStatusReference.md) |  | [optional] 
**deleted_configuration_status** | [**ConfigurationStatusReference**](ConfigurationStatusReference.md) |  | [optional] 
**executive_summary_report_schedule_day** | **int** | Gets or sets             this is only required when scheduleExecutiveSummaryReportFlag &#x3D; true. | [optional] 
**executive_summary_report_schedule_hour** | **int** | Gets or sets             this is only required when scheduleExecutiveSummaryReportFlag &#x3D; true. Input should be in 24 hour format, ie 2pm is 14. | [optional] 
**executive_summary_report_schedule_minute** | **int** | Gets or sets             this is only required when scheduleExecutiveSummaryReportFlag &#x3D; true. | [optional] 
**id** | **int** |  | [optional] 
**integrator_login** | [**IntegratorLoginReference**](IntegratorLoginReference.md) |  | [optional] 
**run_time** | **datetime** |  | [optional] 
**schedule_executive_summary_report_flag** | **bool** |  | 

## Example

```python
from connectwise_psa.models.management import Management

# TODO update the JSON string below
json = "{}"
# create an instance of Management from a JSON string
management_instance = Management.from_json(json)
# print the JSON string representation of the object
print Management.to_json()

# convert the object into a dict
management_dict = management_instance.to_dict()
# create an instance of Management from a dict
management_form_dict = management.from_dict(management_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


