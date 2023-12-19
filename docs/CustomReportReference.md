# CustomReportReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.custom_report_reference import CustomReportReference

# TODO update the JSON string below
json = "{}"
# create an instance of CustomReportReference from a JSON string
custom_report_reference_instance = CustomReportReference.from_json(json)
# print the JSON string representation of the object
print CustomReportReference.to_json()

# convert the object into a dict
custom_report_reference_dict = custom_report_reference_instance.to_dict()
# create an instance of CustomReportReference from a dict
custom_report_reference_form_dict = custom_report_reference.from_dict(custom_report_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


