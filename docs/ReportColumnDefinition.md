# ReportColumnDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_column** | **bool** |  | [optional] 
**is_nullable** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.report_column_definition import ReportColumnDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of ReportColumnDefinition from a JSON string
report_column_definition_instance = ReportColumnDefinition.from_json(json)
# print the JSON string representation of the object
print ReportColumnDefinition.to_json()

# convert the object into a dict
report_column_definition_dict = report_column_definition_instance.to_dict()
# create an instance of ReportColumnDefinition from a dict
report_column_definition_form_dict = report_column_definition.from_dict(report_column_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


