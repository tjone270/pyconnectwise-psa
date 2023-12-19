# ReportCardInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.report_card_info import ReportCardInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReportCardInfo from a JSON string
report_card_info_instance = ReportCardInfo.from_json(json)
# print the JSON string representation of the object
print ReportCardInfo.to_json()

# convert the object into a dict
report_card_info_dict = report_card_info_instance.to_dict()
# create an instance of ReportCardInfo from a dict
report_card_info_form_dict = report_card_info.from_dict(report_card_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


