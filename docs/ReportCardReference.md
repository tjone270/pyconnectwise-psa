# ReportCardReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.report_card_reference import ReportCardReference

# TODO update the JSON string below
json = "{}"
# create an instance of ReportCardReference from a JSON string
report_card_reference_instance = ReportCardReference.from_json(json)
# print the JSON string representation of the object
print ReportCardReference.to_json()

# convert the object into a dict
report_card_reference_dict = report_card_reference_instance.to_dict()
# create an instance of ReportCardReference from a dict
report_card_reference_form_dict = report_card_reference.from_dict(report_card_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


