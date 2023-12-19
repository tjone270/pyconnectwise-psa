# ManagementReportSetup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**scheduled_report_disabled_flag** | **bool** |  | 

## Example

```python
from connectwise_psa.models.management_report_setup import ManagementReportSetup

# TODO update the JSON string below
json = "{}"
# create an instance of ManagementReportSetup from a JSON string
management_report_setup_instance = ManagementReportSetup.from_json(json)
# print the JSON string representation of the object
print ManagementReportSetup.to_json()

# convert the object into a dict
management_report_setup_dict = management_report_setup_instance.to_dict()
# create an instance of ManagementReportSetup from a dict
management_report_setup_form_dict = management_report_setup.from_dict(management_report_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


