# Report


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.report import Report

# TODO update the JSON string below
json = "{}"
# create an instance of Report from a JSON string
report_instance = Report.from_json(json)
# print the JSON string representation of the object
print Report.to_json()

# convert the object into a dict
report_dict = report_instance.to_dict()
# create an instance of Report from a dict
report_form_dict = report.from_dict(report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


