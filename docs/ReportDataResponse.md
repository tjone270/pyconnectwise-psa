# ReportDataResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_definitions** | **List[Dict[str, ReportColumnDefinition]]** |  | [optional] 
**row_values** | **List[List[object]]** |  | [optional] 

## Example

```python
from connectwise_psa.models.report_data_response import ReportDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReportDataResponse from a JSON string
report_data_response_instance = ReportDataResponse.from_json(json)
# print the JSON string representation of the object
print ReportDataResponse.to_json()

# convert the object into a dict
report_data_response_dict = report_data_response_instance.to_dict()
# create an instance of ReportDataResponse from a dict
report_data_response_form_dict = report_data_response.from_dict(report_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


