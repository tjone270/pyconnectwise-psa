# ReportCard


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.report_card import ReportCard

# TODO update the JSON string below
json = "{}"
# create an instance of ReportCard from a JSON string
report_card_instance = ReportCard.from_json(json)
# print the JSON string representation of the object
print ReportCard.to_json()

# convert the object into a dict
report_card_dict = report_card_instance.to_dict()
# create an instance of ReportCard from a dict
report_card_form_dict = report_card.from_dict(report_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


