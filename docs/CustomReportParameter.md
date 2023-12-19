# CustomReportParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**caption_name** | **str** | Either a caption name or parameter name is required. Max length: 50; | [optional] 
**custom_report** | [**CustomReportReference**](CustomReportReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** | Either a caption name or parameter name is required. Max length: 50; | [optional] 

## Example

```python
from connectwise_psa.models.custom_report_parameter import CustomReportParameter

# TODO update the JSON string below
json = "{}"
# create an instance of CustomReportParameter from a JSON string
custom_report_parameter_instance = CustomReportParameter.from_json(json)
# print the JSON string representation of the object
print CustomReportParameter.to_json()

# convert the object into a dict
custom_report_parameter_dict = custom_report_parameter_instance.to_dict()
# create an instance of CustomReportParameter from a dict
custom_report_parameter_form_dict = custom_report_parameter.from_dict(custom_report_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


